import tempfile
from abc import ABC
from os import listdir
from os.path import splitext
from pathlib import Path

from task1.src.singleton import Singleton
from task1.src.storage.metadata import Metadata


class Repository(ABC, Singleton):
    __storage_folder = Path(tempfile.gettempdir()).joinpath('storage')

    def __init__(self, entity_name: str):
        self._path = self.__storage_folder.joinpath(entity_name)
        self._path.mkdir(parents=True, exist_ok=True)
        self._metadata = Metadata(self._path)

    def _get_existing_ids(self):
        ids = list()
        for filename in listdir(self._path):
            json_name = splitext(filename)[0]
            if json_name != 'metadata':
                try:
                    ids.append(int(json_name))
                except ValueError:
                    raise ValueError(f'Incorrect file {filename} in storage')

        return ids

    def _new_entry_id(self):
        return self._metadata.new_entry_id()
