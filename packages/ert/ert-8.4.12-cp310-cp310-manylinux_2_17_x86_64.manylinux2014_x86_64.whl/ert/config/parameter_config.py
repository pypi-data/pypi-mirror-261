from __future__ import annotations

import dataclasses
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple

import xarray as xr

if TYPE_CHECKING:
    from ert.storage import EnsembleReader


class CustomDict(dict):  # type: ignore
    """Used for converting types that can not be serialized
    directly to json
    """

    def __init__(self, data: List[Tuple[Any, Any]]) -> None:
        for i, (key, value) in enumerate(data):
            if isinstance(value, Path):
                data[i] = (key, str(value))
            if isinstance(value, set):
                data[i] = (key, list(value))
        super().__init__(data)


@dataclasses.dataclass
class ParameterConfig(ABC):
    name: str
    forward_init: bool

    def sample_or_load(
        self,
        real_nr: int,
        random_seed: int,
        ensemble_size: int,
    ) -> xr.Dataset:
        return self.read_from_runpath(Path(), real_nr)

    @abstractmethod
    def __len__(self) -> int:
        """Number of parameters"""

    @abstractmethod
    def read_from_runpath(
        self,
        run_path: Path,
        real_nr: int,
    ) -> xr.Dataset:
        """
        This function is responsible for converting the parameter
        from the forward model to the internal ert format
        """

    @abstractmethod
    def write_to_runpath(
        self, run_path: Path, real_nr: int, ensemble: EnsembleReader
    ) -> Optional[Dict[str, Dict[str, float]]]:
        """
        This function is responsible for converting the parameter
        from the internal ert format to the format the forward model
        expects
        """

    def to_dict(self) -> Dict[str, Any]:
        data = dataclasses.asdict(self, dict_factory=CustomDict)
        data["_ert_kind"] = self.__class__.__name__
        return data

    def save_experiment_data(  # noqa: B027
        self,
        experiment_path: Path,
    ) -> None:
        pass
