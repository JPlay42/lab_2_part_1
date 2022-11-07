import unittest
from datetime import datetime, timedelta
from pathlib import Path

from task1.src.storage import EventsRepository
from task1.src.storage.entities.event import Event
from task1.test.storage.repositories.test_repository import RepositoryTest


class EventsRepositoryTest(RepositoryTest):
    __events_dir = RepositoryTest.storage.joinpath(Path('events'))

    def test_init(self):
        EventsRepository()
        self.assertTrue(self.__events_dir.exists())

    def test_create_with_auto_id(self):
        repo = EventsRepository()

        time1 = datetime.now() + timedelta(days=5)
        time2 = time1 + timedelta(days=5)
        self.assertEqual(1, repo.create(Event(None, 'first', time1, 100)))
        self.assertEqual(2, repo.create(Event(None, 'second', time2, 200)))

        expected_event1 = Event(1, 'first', time1, 100)
        expected_event2 = Event(2, 'second', time2, 200)

        received_events = repo.read_all()
        self.assertEqual(expected_event1, received_events[1])
        self.assertEqual(expected_event2, received_events[2])

    def test_create_with_manual_id(self):
        repo = EventsRepository()

        time1 = datetime.now() + timedelta(days=5)
        time2 = time1 + timedelta(days=5)
        event1 = Event(123, 'first', time1, 100)
        event2 = Event(456, 'second', time2, 200)
        repo.create(event1)
        repo.create(event2)

        received_events = repo.read_all()
        self.assertEqual(event1, received_events[123])
        self.assertEqual(event2, received_events[456])

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
