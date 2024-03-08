import asyncio
import math
from dataclasses import dataclass

import nest_asyncio
from shapely.geometry import LineString, Point

from kmService.km_service_builder import KmServiceBuilder
from kmService.models import KmRaai, KmValueObject


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
        nest_asyncio.apply()
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


def get_km_service() -> KmService:
    """
    Retrieves an instance of KmService using asyncio.

    Returns:
        KmService: An instance of KmService.
    """
    return asyncio.run(KmService.factory())
