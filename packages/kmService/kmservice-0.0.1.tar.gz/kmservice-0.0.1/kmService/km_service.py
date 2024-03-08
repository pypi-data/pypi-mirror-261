import asyncio
import math

# import random
from dataclasses import dataclass

import nest_asyncio
from shapely.geometry import LineString, Point

from kmService.km_service_builder import KmServiceBuilder
from kmService.models import KmRaai, KmValueObject

nest_asyncio.apply()


@dataclass
class KmResponse:
    """
    Data class representing a kilometer response.

    Attributes:
        hm: The hectometer value.
        distance: The distance value.
        km_lint_naam: The kilometer lint name.
        km_lint_omschrijving: The kilometer lint description.
        geocode: The geocode value.
        geocode_sub: The sub geocode value.
        geocode_naam: The geocode name.
        xy: The point value.

    """

    hm: float | None = None
    distance: float | None = None
    km_lint_naam: str | None = None
    km_lint_omschrijving: str | None = None
    geocode: int | None = None
    geocode_sub: str | None = None
    geocode_naam: str | None = None
    _raai: KmRaai | None = None
    xy: Point | None = None

    @property
    def display(self) -> str:
        """
        Computes the kilometer value string.
        """
        if self.distance:
            distance = math.floor(self.distance)
            if distance > 100:
                return f"km {self.hm:.3f} +{distance}"
            else:
                if distance < 10:
                    return f"km {self.hm:.1f}0{distance}"
                else:
                    return f"km {self.hm:.1f}{distance}"
        else:
            return "no km"

    @property
    def raai_geometry(self) -> LineString:
        """
        Retrieves the kilometer Raai geometry.
        """
        if self._raai:
            return self._raai.geometry_corrected
        else:
            return LineString()


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

    async def _get_raai(self, point: Point) -> list[KmResponse]:
        async def process(point_, item_):
            if point_.within(item_.geometry):
                response = KmResponse(
                    km_lint_naam=item_.km_vlak.km_lint_naam,
                    km_lint_omschrijving=item_.km_vlak.km_lint_omschrijving,
                    geocode=int(item_.sub_geocode.geo_code),
                    geocode_sub=item_.sub_geocode.sub_code,
                    geocode_naam=item_.sub_geocode.naam,
                )
                distance_raai_to_point = dict(
                    sorted(
                        {
                            _.geometry_corrected.distance(point): _
                            for _ in item_.km_raaien
                        }.items()
                    )
                )
                first_two = [
                    distance_raai_to_point[k] for k in list(distance_raai_to_point)[:2]
                ]
                if first_two[0].hectometer < first_two[1].hectometer:
                    response._raai = first_two[0]
                    return response
                else:
                    response._raai = first_two[1]
                    return response

        tasks = []
        tasks.extend(
            [process(point, item) for item in self._value_objects_dict.values()]
        )
        result = await asyncio.gather(*tasks)
        return [item for item in result if item is not None]

    async def _get_km_async(self, x: float, y: float) -> list[KmResponse]:
        _ = []
        point = Point(x, y)
        responses = await self._get_raai(point)
        for response in responses:
            projection_point = response.raai_geometry.interpolate(
                response.raai_geometry.project(point)
            )
            if response._raai is not None:
                hm = response._raai.hectometer
            else:
                hm = 0.0
            response.hm = hm
            response.xy = point
            distance = projection_point.distance(point)
            response.distance = distance
            _.append(response)
        return _

    def get_km(self, x: float, y: float) -> list[KmResponse]:
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

    async def _get_km_batch_async(self, point_list) -> list[list[KmResponse]]:
        tasks = [self._get_km_async(point[0], point[1]) for point in point_list]
        results = await asyncio.gather(*tasks)
        return [result for result in results]

    def get_km_batch(
        self, point_list: list[list[int | float]]
    ) -> list[list[KmResponse]]:
        """
        Retrieves KM responses synchronously for a batch of points.

        Args:
            point_list: A list of lists containing the coordinates of points.

        Returns:
            A list of lists containing KM responses for each point.
        """
        response = asyncio.run(self._get_km_batch_async(point_list))
        return response

    # async def get_point(
    #     self, lintnaam: str, km: float, m: int, line_geometry: LineString
    # ):
    #     features = []
    #     features.append(
    #         GeoJsonFeature(
    #             [ShapelyTransform.rd_to_wgs(line_geometry)],
    #             {"type": "input_line_geometry"},
    #         )
    #     )
    #
    #     posible_matches = list(
    #         itertools.chain.from_iterable(
    #             [
    #                 value.km_raaien
    #                 for key, value in self._value_objects_dict.items()
    #                 if key.endswith(lintnaam)
    #             ]
    #         )
    #     )
    #
    #     # Initialize variables to hold the objects before and after the input value
    #     object_before = None
    #     object_after = None
    #     input_value = km
    #     # Iterate through the list of objects
    #
    #     # Initialize variables to hold the minimum differences
    #     min_difference_before = float("inf")
    #     min_difference_after = float("inf")
    #
    #     raai_to_project_from = [obj for obj in posible_matches if obj.hectometer == km][
    #         0
    #     ]
    #     features.append(
    #         GeoJsonFeature(
    #             [ShapelyTransform.rd_to_wgs(raai_to_project_from.geometry_corrected)],
    #             {"type": "raai_to_project_from"},
    #         )
    #     )
    #
    #     # Iterate through the list of objects
    #     for obj in posible_matches:
    #         difference = abs(obj.hectometer - input_value)
    #         if obj.hectometer < input_value and difference < min_difference_before:
    #             min_difference_before = difference
    #             object_before = obj
    #         elif obj.hectometer > input_value and difference < min_difference_after:
    #             min_difference_after = difference
    #             object_after = obj
    #
    #     # Check if objects were found before and/or after the input value
    #     if object_before:
    #         print("Object before:", object_before.hectometer)
    #     else:
    #         print("No object before")
    #
    #     if object_after:
    #         print("Object after:", object_after.hectometer)
    #     else:
    #         print("No object after")
    #     features.append(
    #         GeoJsonFeature(
    #             [ShapelyTransform.rd_to_wgs(object_before.geometry_corrected)],
    #             {"type": "object_before"},
    #         )
    #     )
    #
    #     # Define the reference line
    #     reference_line = raai_to_project_from.geometry_corrected
    #     features.append(
    #         GeoJsonFeature(
    #             [ShapelyTransform.rd_to_wgs(reference_line)], {"type": "reference_line"}
    #         )
    #     )
    #
    #     # Define the target line
    #     target_line = object_after.geometry_corrected
    #     features.append(
    #         GeoJsonFeature(
    #             [ShapelyTransform.rd_to_wgs(target_line)], {"type": "target_line"}
    #         )
    #     )
    #
    #     # Find the nearest points on both lines
    #     nearest_point_on_reference, nearest_point_on_target = nearest_points(
    #         reference_line, target_line
    #     )
    #
    #     # Calculate the vector from the reference line's starting point to the nearest point on the target line
    #     dx_nearest = nearest_point_on_target.coords[0][0] - reference_line.coords[0][0]
    #     dy_nearest = nearest_point_on_target.coords[0][1] - reference_line.coords[0][1]
    #     unit_direction_nearest = np.array([dx_nearest, dy_nearest]) / np.linalg.norm(
    #         [dx_nearest, dy_nearest]
    #     )
    #
    #     # Determine the direction perpendicular to the target line at the nearest point
    #     # perpendicular_dir_nearest = np.array([-dy_nearest, dx_nearest])
    #     # unit_perpendicular_dir_nearest = perpendicular_dir_nearest / np.linalg.norm(
    #     #     perpendicular_dir_nearest
    #     # )
    #
    #     # Define the distance to move the reference line
    #     distance = (
    #         m + 0.001 if m != 0 else m
    #     )  # Adjust it a bit so it is not just under.
    #
    #     # Move the reference line towards the target line
    #     movement_vector_nearest = unit_direction_nearest * distance
    #     moved_reference_line = translate(
    #         reference_line, movement_vector_nearest[0], movement_vector_nearest[1]
    #     )
    #     features.append(
    #         GeoJsonFeature(
    #             [ShapelyTransform.rd_to_wgs(moved_reference_line)],
    #             {"type": "moved_reference_line"},
    #         )
    #     )
    #
    #     print("Original Reference Line:", reference_line)
    #     print("Moved Reference Line:", moved_reference_line)
    #
    #     point = line_geometry.intersection(moved_reference_line)
    #     features.append(
    #         GeoJsonFeature([ShapelyTransform.rd_to_wgs(point)], {"type": "point"})
    #     )
    #
    #     fc = GeoJsonFeatureCollection(features)
    #     tester = dumps(fc)
    #     print(tester)
    #
    #     return point

    # def generate_geojson_output(self, file_name: str | None = None) -> str:
    #     """
    #     Generates GeoJSON output based on the data stored in KmService.
    #
    #     Returns:
    #         str: A GeoJSON string representing the data.
    #     """
    #     colors = [
    #         "#1F77B4",
    #         "#AEC7E8",
    #         "#FF7F0E",
    #         "#FFBB78",
    #         "#2CA02C",
    #         "#98DF8A",
    #         "#FF9896",
    #         "#9467BD",
    #         "#C5B0D5",
    #         "#8C564B",
    #         "#C49C94",
    #         "#E377C2",
    #         "#F7B6D2",
    #         "#7F7F7F",
    #         "#C7C7C7",
    #         "#BCBD22",
    #         "#DBDB8D",
    #         "#17BECF",
    #         "#9EDAE5",
    #     ]
    #
    #     features = []
    #     for key, value in self._value_objects_dict.items():
    #         picked_color = random.choice(colors)
    #         features.append(
    #             GeoJsonFeature(
    #                 [ShapelyTransform.rd_to_wgs(value.geometry)],
    #                 {
    #                     "color": picked_color,
    #                     "fill-color": "transparent",
    #                     "fill-opacity": 0.5,
    #                 },
    #             )
    #         )
    #
    #         for item in value.matched:
    #             if not item[1]:
    #                 features.append(
    #                     GeoJsonFeature(
    #                         [ShapelyTransform.rd_to_wgs(item[0].geometry)],
    #                         {"color": "red", "radius": "5px"},
    #                     )
    #                 )  # | item[0].__dict__))
    #             else:
    #                 features.append(
    #                     GeoJsonFeature(
    #                         [ShapelyTransform.rd_to_wgs(item[0].geometry)],
    #                         {"color": picked_color, "radius": "1px"},
    #                     )
    #                 )
    #
    #                 # features.append(GeoJsonFeature([ShapelyTransform.rd_to_wgs(item[1].geometry_extended)], {"color": "#5c5c5c"}))
    #                 features.append(
    #                     GeoJsonFeature(
    #                         [ShapelyTransform.rd_to_wgs(item[1].geometry)],
    #                         {"color": "#c9c9c9"},
    #                     )
    #                 )
    #                 features.append(
    #                     GeoJsonFeature(
    #                         [ShapelyTransform.rd_to_wgs(item[1].geometry_corrected)],
    #                         {"color": picked_color},
    #                     )
    #                 )
    #     _ = dumps(GeoJsonFeatureCollection(features))
    #     if file_name is not None:
    #         with open(file_name, "w") as text_file:
    #             text_file.write(_)
    #     return _


def get_km_service() -> KmService:
    """
    Retrieves an instance of KmService using asyncio.

    Returns:
        KmService: An instance of KmService.
    """
    return asyncio.run(KmService.factory())
