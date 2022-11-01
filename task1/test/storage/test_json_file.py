import json
import tempfile
import unittest
from os import remove
from pathlib import Path

from task1.src.storage.json_file import JsonFile


class JsonFileTest(unittest.TestCase):
    __temp_dir = Path(tempfile.gettempdir())
    __temp_file = __temp_dir.joinpath('test.json')

    def setUp(self):
        if self.__temp_file.exists():
            remove(self.__temp_file)

    def test_init_with_suffix(self):
        self.assertFalse(self.__temp_file.exists())
        JsonFile(self.__temp_dir, 'test.json')
        self.assertTrue(self.__temp_file.exists())

    def test_init_without_suffix(self):
        self.assertFalse(self.__temp_file.exists())
        JsonFile(self.__temp_dir, 'test')
        self.assertTrue(self.__temp_file.exists())

    def test_read_all(self):
        with open(self.__temp_file, 'w') as file:
            json.dump({'name': 'value'}, file)

        json_file = JsonFile(self.__temp_dir, 'test')
        content = json_file.read_all()
        self.assertEqual('value', content['name'])

    def test_read(self):
        with open(self.__temp_file, 'w') as file:
            json.dump({'name': 'value'}, file)

        json_file = JsonFile(self.__temp_dir, 'test')
        self.assertEqual('value', json_file.read('name'))

    def test_increment_and_get(self):
        with open(self.__temp_file, 'w') as file:
            json.dump({'count': 9}, file)

        json_file = JsonFile(self.__temp_dir, 'test')
        self.assertEqual(10, json_file.increment_and_get('count'))

        with open(self.__temp_file, 'r') as file:
            content = json.load(file)
            self.assertEqual(10, content['count'])

    def test_write(self):
        json_file = JsonFile(self.__temp_dir, 'test')
        json_file.write('name', 'value')

        with open(self.__temp_file, 'r') as file:
            content = json.load(file)
            self.assertEqual('value', content['name'])

    def test_write_all(self):
        json_file = JsonFile(self.__temp_dir, 'test')
        json_file.write_all({'name': 'value'})

        with open(self.__temp_file, 'r') as file:
            content = json.load(file)
            self.assertEqual('value', content['name'])


if __name__ == '__main__':
    unittest.main()
