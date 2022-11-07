import tempfile
import unittest
from pathlib import Path
from shutil import rmtree


class RepositoryTest(unittest.TestCase):
    storage = Path(tempfile.gettempdir()).joinpath(Path('tickets_storage'))

    @staticmethod
    def __remove_storage():
        if RepositoryTest.storage.exists():
            rmtree(RepositoryTest.storage)

    def setUp(self):
        self.__remove_storage()

    @classmethod
    def tearDownClass(cls):
        cls.__remove_storage()


if __name__ == '__main__':
    unittest.main()
