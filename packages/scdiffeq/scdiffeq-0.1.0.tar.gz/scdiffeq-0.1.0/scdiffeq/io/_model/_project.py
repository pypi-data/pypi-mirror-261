
# -- import packages: ---------------------------------------------------------
import ABCParse
import pathlib


# -- import local dependencies: -----------------------------------------------
from ._version import Version


# -- set typing: --------------------------------------------------------------
from typing import Dict, Union


# -- operational class: -------------------------------------------------------
class Project(ABCParse.ABCParse):
    """Object container for an scDiffEq project"""

    def __init__(
        self,
        path: Union[str, pathlib.Path] = pathlib.Path("./").absolute(),
        metrics_groupby: str = "epoch",
        *args,
        **kwargs,
    ):
        """Initialize the project object by providing a path.

        Args:
            path (pathlib.Path): path to the project, created by scDiffeq.

        Returns:
            None
        """
        self.__parse__(locals())

        self._set_version_path_attributes()

    @property
    def _PROJECT_PATH(self) -> pathlib.Path:
        """check and format the provided project path"""
        if isinstance(self._path, pathlib.Path):
            return self._path
        elif isinstance(self._path, str):
            return pathlib.Path(self._path)
        else:
            raise TypeError("arg: `path` must be of type: [pathlib.Path, str]")

    @property
    def _VERSION_PATHS(self) -> Dict[str, pathlib.Path]:
        """Assemble available version paths based on the provided project path"""
        version_paths = sorted(list(self._PROJECT_PATH.glob("version_*")))
        return {path.name: path for path in version_paths}

    def _set_version_path_attributes(self) -> None:
        """sets the name of each version as a cls attribute, pointing to the
        path of the version."""
        for v_name, v_path in self._VERSION_PATHS.items():
            version = Version(path = v_path, groupby = self._metrics_groupby)
            setattr(self, v_name, version)
            
    def __getitem__(self, version: int) -> pathlib.Path:
        """format version key and return version"""
        return getattr(self, f"version_{version}")

    def __repr__(self) -> str:
        """return the name of the obj"""
        return """scDiffEq Project"""
