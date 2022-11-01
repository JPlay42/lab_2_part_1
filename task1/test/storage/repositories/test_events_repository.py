import unittest
from pathlib import Path
from shutil import rmtree

from task1.src.storage import EventsRepository


class EventsRepositoryTest(unittest.TestCase):
    __events_dir = Path('../../../storage/events')

    def setUp(self):
        if self.__events_dir.exists():
            rmtree(self.__events_dir)

    def test_init(self):
        EventsRepository()
        self.assertTrue(self.__events_dir.exists())


if __name__ == '__main__':
    unittest.main()
