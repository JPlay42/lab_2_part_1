import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from shutil import rmtree

from task1.src.storage import TicketsRepository, EventsRepository
from task1.src.storage.entities.event import Event
from task1.src.storage.entities.ticket import Ticket
from task1.src.storage.json_file import JsonFile


class TicketsRepositoryTest(unittest.TestCase):
    __tickets_dir = Path(tempfile.gettempdir()).joinpath(Path('storage/tickets'))

    def setUp(self):
        storage = self.__tickets_dir.parent
        if storage.exists():
            rmtree(storage)

    def test_init(self):
        TicketsRepository()
        self.assertTrue(self.__tickets_dir.exists())

    def test_create(self):
        tickets_repo = TicketsRepository()

        event = self.default_event()
        ticket = Ticket.of(None, event, 'Ivan Kuruch', datetime.now(), True)
        ticket_id = tickets_repo.create(ticket)

        json_file = JsonFile(self.__tickets_dir, f'{ticket_id}.json')
        content = json_file.read_all()
        self.assertEqual(event.id, content['event_id'])
        self.assertEqual(ticket.name, content['name'])
        self.assertEqual(ticket.date.isoformat(), content['date'])
        self.assertEqual(ticket.is_student, content['is_student'])

    def test_read(self):
        repo = TicketsRepository()

        event = self.default_event()
        ticket = Ticket.of(1, event, 'Ivan Kuruch', datetime.now(), True)
        repo.create(ticket)
        self.assertEqual(ticket, repo.read(ticket.id))

    def test_read_all(self):
        repo = TicketsRepository()

        event = self.default_event()
        first_ticket = Ticket.of(1, event, 'Ivan Kuruch', datetime.now(), True)
        second_ticket = Ticket.of(2, event, 'Mykola Pylypchuk', datetime.now() - timedelta(days=3), True)
        repo.create(first_ticket)
        repo.create(second_ticket)
        received_tickets = repo.read_all()
        self.assertEqual(2, len(received_tickets))

        for key in received_tickets:
            self.assertEqual(repo.read(key), received_tickets[key])

    def test_update(self):
        repo = TicketsRepository()

        now = datetime.now()
        event = self.default_event()
        ticket = Ticket.of(1, event, 'Ivan Kuruch', now, True)
        repo.create(ticket)
        self.assertEqual(ticket, repo.read(ticket.id))

        edited_ticket = Ticket.of(1, event, 'Jason Statham', now, True)
        repo.update(edited_ticket)
        self.assertEqual(edited_ticket, repo.read(edited_ticket.id))

    def test_delete(self):
        repo = TicketsRepository()

        event = self.default_event()
        ticket = Ticket.of(1, event, 'Nicolas Brown', datetime.now(), False)
        repo.create(ticket)
        self.assertEqual(1, len(repo.read_all()))

        repo.delete(ticket.id)
        self.assertEqual(0, len(repo.read_all()))

    @staticmethod
    def default_event():
        events_repo = EventsRepository()
        return events_repo.read(
            events_repo.create(
                Event(None, 'Google HashCode', datetime.now() + timedelta(days=14), 30)
            )
        )


if __name__ == '__main__':
    unittest.main()
