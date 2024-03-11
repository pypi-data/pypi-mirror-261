import asyncio
import itertools

import nest_asyncio
import numpy as np
from shapely.affinity import translate
from shapely.geometry import LineString, Point
from shapely.ops import nearest_points

from kmService import KmLintMeasure
from kmService.km_models import KmValueObject
from kmService.km_responses import KmResponse, PointInputResponse, PointResponse
from kmService.km_service_builder import KmServiceBuilder

nest_asyncio.apply()


class KmService:
    """
    A service class for calculating kilometers and related features.
    """

    def __init__(self):
        self._value_objects_dict: dict[str, KmValueObject] = {}

    @classmethod
    async def factory(cls):
        """
        Factory method to create an instance of KmService.

        Returns:
            KmService: An instance of KmService.
        """
        self = cls()
        km_service = await KmServiceBuilder.factory(
            "https://maps.prorail.nl/arcgis/rest/services/Referentiesysteem/FeatureServer"
        )
        self._value_objects_dict = km_service.value_objects
        return self

    async def _get_raaien_to_measure(self, point: Point) -> KmResponse:
        # in some cases we can have more than  one set of raaien (flyover situation)
        async def process(point_, item_):
            if point_.within(item_.geometry):
                init_response = KmLintMeasure.from_value_object(item_, point)

                # find closest 2 raaien pick lowest
                distance_raai_to_point = dict(
                    sorted(
                        {
                            raai.geometry_corrected.distance(point): raai
                            for raai in item_.km_raaien
                        }.items()
                    )
                )
                closest_two_raaien = [
                    distance_raai_to_point[k] for k in list(distance_raai_to_point)[:2]
                ]
                if closest_two_raaien[0].hectometer < closest_two_raaien[1].hectometer:
                    init_response.raai = closest_two_raaien[0].geometry_corrected
                    init_response.hm = closest_two_raaien[0].hectometer
                    return init_response
                else:
                    init_response.raai = closest_two_raaien[1].geometry_corrected
                    init_response.hm = closest_two_raaien[1].hectometer
                    return init_response

        tasks = []
        tasks.extend(
            [process(point, item) for item in self._value_objects_dict.values()]
        )
        result = await asyncio.gather(*tasks)
        return KmResponse(point, [item for item in result if item is not None])

    async def _get_km_async(self, x: float, y: float) -> KmResponse:
        point = Point(x, y)
        responses = await self._get_raaien_to_measure(point)
        for response in responses.km_measures:
            projection_point = response.raai.interpolate(response.raai.project(point))
            distance = projection_point.distance(point)
            response.distance = distance
        return responses

    def get_km(self, x: float, y: float) -> KmResponse:
        """
        Retrieves kilometer responses based on the provided coordinates.

        Args:
            x: The x-coordinate.
            y: The y-coordinate.

        Returns:
            A list of kilometer responses.
        """
        response = asyncio.run(self._get_km_async(x, y))
        return response

    async def _get_km_batch_async(self, point_list) -> list[KmResponse]:
        tasks = [self._get_km_async(point[0], point[1]) for point in point_list]
        results = await asyncio.gather(*tasks)
        return [result for result in results]

    def get_km_batch(self, point_list: list[list[int | float]]) -> list[KmResponse]:
        """
        Retrieves KM responses synchronously for a batch of points.

        Args:
            point_list: A list of lists containing the coordinates of points.

        Returns:
            A list of lists containing KM responses for each point.
        """
        response = asyncio.run(self._get_km_batch_async(point_list))
        return response

    def get_point(
        self, lint_name: str, km: float, m: int, line_geometry: LineString
    ) -> PointResponse:
        """

        Get a projected point on the line.


            1. Get all raaien associated with the input lint.
            2. Find the closest raaien: the one before and after the specified kilometer measure.
            3. Calculate reference and target raai: based on the hm found before and after.
                a. if no next we use raai before and negative distance to project.
            4. Find nearest points of the reference line and the target line.
            5. Calculate movement vector from the nearest points.
            6. Move the reference line towards the target line.
            j. Calculate projected point: intersection point of the input line geometry with the moved reference line.

        !!! warning

            This feature is experimental and may not be suitable for production use.
            Ensure to thoroughly test this feature with your data before deploying it.

        Args:
            lint_name (str): The name of the lint.
            km (float): Kilometer measure.
            m (int): Distance value.
            line_geometry (LineString): The geometry of the line.

        Returns:
            PointResponse: Response containing projected point information.
        """
        lint_raaien = list(
            itertools.chain.from_iterable(
                [
                    value.km_raaien
                    for key, value in self._value_objects_dict.items()
                    if key.endswith(lint_name)
                ]
            )
        )

        # Initialize variables to hold the objects before and after the input value
        object_before = None
        object_after = None

        # Initialize variables to hold the minimum differences
        min_difference_before = float("inf")
        min_difference_after = float("inf")

        # get raai of interest
        raai_to_project_from = [_ for _ in lint_raaien if _.hectometer == km][0]

        # debug geojson
        reference_line = raai_to_project_from.geometry_corrected

        # Iterate through the list of objects get raai before and after...
        for obj in lint_raaien:
            difference = abs(obj.hectometer - km)
            if obj.hectometer < km and difference < min_difference_before:
                min_difference_before = difference
                object_before = obj
            elif obj.hectometer > km and difference < min_difference_after:
                min_difference_after = difference
                object_after = obj

        # Check if objects were found before and/or after the input value
        if object_before:
            print("Object before:", object_before.hectometer)
        else:
            print("No object before")

        if object_after:
            print("Object after:", object_after.hectometer)
        else:
            print("No object after")

        # Determine the line to project towards
        if object_after:
            target_line = object_after.geometry_corrected
        elif object_before:
            # use before and make movement negative so offset point the right direction
            target_line = object_before.geometry_corrected
            m *= -1
        else:
            raise NotImplementedError("can not handle single raai in lint.")

        # Find the nearest points on both lines
        nearest_point_reference, nearest_point_target = nearest_points(
            reference_line, target_line
        )

        # Calculate the vector from the reference line's starting point to the nearest point on the target line
        dx_nearest = (
            nearest_point_target.coords[0][0] - nearest_point_reference.coords[0][0]
        )
        dy_nearest = (
            nearest_point_target.coords[0][1] - nearest_point_reference.coords[0][1]
        )
        unit_direction_nearest = np.array([dx_nearest, dy_nearest]) / np.linalg.norm(
            [dx_nearest, dy_nearest]
        )

        # Define the distance to move the reference line
        distance = (
            m - 0.001 if m < 0 else m + 0.001 if m > 0 else m
        )  # Adjust it a bit so it is not just under.

        # Move the reference line towards the target line
        movement_vector_nearest = unit_direction_nearest * distance
        moved_reference_line = translate(
            reference_line, movement_vector_nearest[0], movement_vector_nearest[1]
        )

        projected_point = line_geometry.intersection(moved_reference_line)

        return PointResponse(
            input_data=PointInputResponse(
                input_line=line_geometry,
                input_lint_name=lint_name,
                input_km=km,
                input_distance=m,
            ),
            km_line=moved_reference_line,
            km_point=projected_point,
            reference_line=reference_line,
        )

    def get_unique_lint_names(self) -> list[str]:
        """
        Get all unique lint names.

        Returns:
            A list of unique lint names.
        """
        return list(
            set(
                [
                    value.km_vlak.km_lint_naam
                    for key, value in self._value_objects_dict.items()
                ]
            )
        )


def get_km_service() -> KmService:
    """
    Retrieves an instance of KmService using asyncio.

    Returns:
        KmService: An instance of KmService.
    """
    return asyncio.run(KmService.factory())
