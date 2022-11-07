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

    def test_generate_id(self):
        metadata = Metadata(self.__temp_dir)
        for i in range(1, 6):
            self.assertEqual(i, metadata.generate_id())

        self.assertEqual(5, len(metadata.get_existing_ids()))

    def test_add_custom_id(self):
        metadata = Metadata(self.__temp_dir)
        for i in range(3):
            metadata.generate_id()
        for i in range(1, 4):
            self.assertFalse(metadata.add_custom_id(i))

        self.assertTrue(metadata.add_custom_id(4))
        self.assertTrue(metadata.add_custom_id(10))
        self.assertFalse(metadata.add_custom_id(10))
        self.assertFalse(metadata.add_custom_id(4))

        self.assertEqual(5, metadata.generate_id())

    def test_get_all_ids(self):
        metadata = Metadata(self.__temp_dir)

        for i in range(3):
            metadata.generate_id()
        metadata.add_custom_id(5)

        expected_ids = [1, 2, 3, 5]
        self.assertEqual(expected_ids, metadata.get_existing_ids())

    def test_delete_id(self):
        metadata = Metadata(self.__temp_dir)

        for i in range(3):
            metadata.generate_id()
        metadata.add_custom_id(5)
        metadata.add_custom_id(8)
        metadata.delete_id(2)
        metadata.delete_id(5)

        expected_ids = [1, 3, 8]
        self.assertEqual(expected_ids, metadata.get_existing_ids())


if __name__ == '__main__':
    unittest.main()
