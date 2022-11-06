import json
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from shutil import rmtree

from task1.src.storage import EventsRepository
from task1.src.storage.entities.event import Event


class EventsRepositoryTest(unittest.TestCase):
    __events_dir = Path(tempfile.gettempdir()).joinpath(Path('storage/events'))

    def setUp(self):
        if self.__events_dir.exists():
            rmtree(self.__events_dir)

    def test_init(self):
        EventsRepository()
        self.assertTrue(self.__events_dir.exists())

    def test_create(self):
        repo = EventsRepository()

        time1 = datetime.now() + timedelta(days=5)
        time2 = time1 + timedelta(days=5)
        self.assertEqual(1, repo.create(Event(None, 'first', time1, 100)))
        self.assertEqual(2, repo.create(Event(None, 'second', time2, 200)))

        first_path = self.__events_dir.joinpath('1.json')
        self.assertTrue(first_path.exists())
        with open(first_path, 'r') as file:
            content = json.load(file)
            self.assertEqual('first', content['name'])
            self.assertEqual(time1.isoformat(), content['date'])
            self.assertEqual(100, content['price'])

        second_path = self.__events_dir.joinpath('2.json')
        self.assertTrue(second_path.exists())
        with open(second_path, 'r') as file:
            content = json.load(file)
            self.assertEqual('second', content['name'])
            self.assertEqual(time2.isoformat(), content['date'])
            self.assertEqual(200, content['price'])

    def test_read(self):
        repo = EventsRepository()

        created_event = Event(None, 'Event name', datetime.now() + timedelta(days=5), 128)
        event_id = repo.create(created_event)

        received_event = repo.read(event_id)
        self.assertEqual(event_id, received_event.id)
        self.assertEqual(created_event.name, received_event.name)
        self.assertEqual(created_event.date, received_event.date)
        self.assertEqual(created_event.price, received_event.price)

    def test_read_all(self):
        repo = EventsRepository()

        time1 = datetime.now() + timedelta(days=5)
        time2 = time1 + timedelta(days=5)

        first_event = Event(None, 'first', time1, 100)
        second_event = Event(None, 'second', time2, 200)
        repo.create(first_event)
        repo.create(second_event)
        received_events = repo.read_all()
        self.assertEqual(2, len(received_events))

        for key in received_events:
            self.assertEqual(repo.read(key), received_events[key])

    def test_update(self):
        repo = EventsRepository()

        time1 = datetime.now() + timedelta(days=1)
        time2 = time1 + timedelta(days=1)

        event = Event(None, 'Event name', time1, 123)
        event_id = repo.create(event)

        updated_event = Event(event_id, event.name, time2, event.price)
        repo.update(updated_event)
        received_updated_event = repo.read(event_id)
        self.assertEqual(updated_event, received_updated_event)

    def test_delete(self):
        repo = EventsRepository()

        event = Event(None, 'Event name', datetime.now() + timedelta(days=5), 123)
        event_id = repo.create(event)
        events = repo.read_all()
        self.assertEqual(1, len(events))

        repo.delete(event_id)
        events = repo.read_all()
        self.assertEqual(0, len(events))


if __name__ == '__main__':
    unittest.main()
