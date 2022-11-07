import tempfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TypeVar, Generic

from task1.src.singleton import Singleton
from task1.src.storage.metadata import Metadata

T = TypeVar('T')


class Repository(ABC, Singleton, Generic[T]):
    __storage_folder = Path(tempfile.gettempdir()).joinpath('storage')

    @abstractmethod
    def create(self, entry: T):
        pass

    @abstractmethod
    def read(self, entry_id: int):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, entry: T):
        pass

    @abstractmethod
    def delete(self, entry_id: int):
        pass

    def __init__(self, entity_name: str):
        self._path = self.__storage_folder.joinpath(entity_name)
        self._path.mkdir(parents=True, exist_ok=True)
        self._metadata = Metadata(self._path)

    def get_existing_ids(self):
        return self._metadata.get_existing_ids()

    def generate_id(self):
        return self._metadata.generate_id()

    def add_custom_id(self, custom_id: int):
        return self._metadata.add_custom_id(custom_id)

    def delete_id(self, id_to_delete: int):
        return self._metadata.delete_id(id_to_delete)
