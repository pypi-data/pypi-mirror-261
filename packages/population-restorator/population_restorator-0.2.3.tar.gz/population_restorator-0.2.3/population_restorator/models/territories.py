"""City territories class and methods are defined here."""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from loguru import logger


@dataclass
class Territory:
    """City inner or outer territory either with the next level territory or with buildings.

    Multiple territories layers can be represented this way, starting with the city itself.

    houses must contain 'living_area' (float) column for the proper work.
    """

    name: str
    population: int | None
    inner_territories: list["Territory"] | None = None
    houses: pd.DataFrame | None = None

    def get_total_living_area(self) -> float:
        """Get total living area of all houses of the territory (its inner territories)."""
        if self.inner_territories is not None:
            return sum(it.get_total_living_area() for it in self.inner_territories)
        return self.houses["living_area"].sum() if not self.houses.empty else 0.0

    def get_total_territories_population(self) -> int:
        """Get total populaton of the lower level of territories."""
        if self.inner_territories is None:
            return self.population
        populations = [it.get_total_territories_population() for it in self.inner_territories]
        if None in populations:
            return self.population
        return sum(populations)

    def get_all_houses(self) -> pd.DataFrame:
        """Get single DataFrame containing all inner territories houses."""
        if self.inner_territories is None:
            return self.houses
        it_with_houses = list(
            filter(lambda df: df.shape[0] > 0, (it.get_all_houses() for it in self.inner_territories))
        )
        if len(it_with_houses) > 0:
            return pd.concat(it_with_houses).reset_index(drop=True)
        if len(self.inner_territories) == 0:
            return pd.DataFrame()
        return self.inner_territories[0].get_all_houses()

    def get_total_houses_population(self, raise_on_population_missing: bool = True) -> int:
        """Get total population of all territories houses. Will throw ValueError if not each of the houses
        DataFrames have 'population' column and `raise_on_population_missing` is set to True. Otherwise will
        ignore buildings without 'population' column.
        """
        if self.inner_territories is not None:
            return sum(it.get_total_houses_population() for it in self.inner_territories)

        if "population" not in self.houses.columns:
            if raise_on_population_missing:
                raise ValueError(f"Buildings of a territory '{self.name}' do not have 'population' column")
            return 0

        try:
            return int(self.houses["population"].sum())
        except Exception as exc:  # pylint: disable=broad-except
            logger.warning("Could not return sum of territory '{}' houses population: {!r}", self.name, exc)
            if raise_on_population_missing:
                raise ValueError(f"Could not get summary population of a tettiroty '{self.name}'") from exc
            return 0

    def copy(self) -> "Territory":
        """Create a deep copy of the territory."""
        return Territory(
            self.name,
            self.population,
            ([it.copy() for it in self.inner_territories] if self.inner_territories is not None else None),
            (self.houses.copy() if self.houses is not None else None),
        )

    def __str__(self) -> str:
        return (
            f"Territory(name='{self.name}', population='{self.population}',"
            f" inner_territories_count={len(self.inner_territories) if self.inner_territories is not None else 0},"
            f" houses_count={self.houses.shape[0] if self.houses is not None else 0})"
        )

    def deep_info(self) -> dict:
        """Return deep info of a given territory as a dict with keys: `name`, `population`, `inner_territories`
        and `houses`.

        `inner_territories` value can be None or a list of dicts of the same format.
        """
        return {
            "name": self.name,
            "population": self.population,
            "inner_territories": (
                [it.deep_info() for it in self.inner_territories] if self.inner_territories is not None else None
            ),
            "houses": (
                {
                    "count": self.houses.shape[0],
                    "living_area": self.houses["living_area"].sum(),
                }
                if self.houses is not None
                else None
            ),
        }
