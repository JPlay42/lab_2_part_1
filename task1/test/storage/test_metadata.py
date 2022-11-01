import json
import tempfile
import unittest
from os import remove
from pathlib import Path

from task1.src.storage.metadata import Metadata


class MetadataTest(unittest.TestCase):
    __temp_dir = Path(tempfile.gettempdir())
    __temp_file = __temp_dir.joinpath('metadata.json')

    def setUp(self):
        if self.__temp_file.exists():
            remove(self.__temp_file)

    def test_init(self):
        self.assertFalse(self.__temp_file.exists())
        Metadata(self.__temp_dir)
        self.assertTrue(self.__temp_file.exists())

    def test_new_entry_id(self):
        metadata = Metadata(self.__temp_dir)
        for i in range(1, 6):
            self.assertEqual(i, metadata.new_entry_id())

        with open(self.__temp_file, 'r') as file:
            content = json.load(file)
            self.assertEqual(5, content['entries_count'])


if __name__ == '__main__':
    unittest.main()
