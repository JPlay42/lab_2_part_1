import tempfile
from abc import ABC
from pathlib import Path

from task1.src.singleton import Singleton
from task1.src.storage.metadata import Metadata


class Repository(ABC, Singleton):
    __storage_folder = Path(tempfile.gettempdir()).joinpath('storage')

    def __init__(self, entity_name: str):
        self._path = self.__storage_folder.joinpath(entity_name)
        self._path.mkdir(parents=True, exist_ok=True)
        self._metadata = Metadata(self._path)

    def _new_entry_id(self):
        return self._metadata.new_entry_id()
