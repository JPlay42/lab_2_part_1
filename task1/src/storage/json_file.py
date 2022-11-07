import json
from json import JSONDecodeError
from pathlib import Path


class JsonFile:
    def __init__(self, folder: Path, name: str):
        name = name.removesuffix('.json')
        self.__path = folder.joinpath(f'{name}.json')
        if not self.__path.exists():
            self._create_file()
            self._post_create()

    def _post_create(self):
        pass

    def _create_file(self):
        if not self.__path.exists():
            file = open(self.__path, 'w')
            file.close()

    def read_all(self):
        with open(self.__path, 'r') as file:
            try:
                return json.load(file)
            except JSONDecodeError:
                return dict()

    def read(self, name: str):
        return self.read_all()[name]

    def write(self, name: str, value):
        content = self.read_all()
        content[name] = value
        self.write_all(content)

    def write_all(self, content: dict):
        with open(self.__path, 'w') as file:
            json.dump(content, file)
