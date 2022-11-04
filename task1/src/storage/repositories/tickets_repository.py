from datetime import datetime
from os import listdir, remove
from os.path import splitext

from task1.src.storage import EventsRepository
from task1.src.storage.entities.event import Event
from task1.src.storage.entities.ticket import Ticket
from task1.src.storage.json_file import JsonFile
from task1.src.storage.repositories.repository import Repository


class TicketsRepository(Repository):
    __events_repository = EventsRepository()

    def __init__(self):
        super().__init__('tickets')

    def create(self, ticket: Ticket):
        if ticket.id is None:
            ticket_id = self._new_entry_id()
        else:
            ticket_id = ticket.id
        file = JsonFile(self._path, str(ticket_id))
        file.write_all(self.__ticket_to_dict(ticket))
        return ticket_id

    def read(self, ticket_id: int):
        json_file = JsonFile(self._path, str(ticket_id))
        content = json_file.read_all()
        event = self.__events_repository.read(content['event_id'])
        return self.__dict_to_ticket(ticket_id, content, event)

    def read_all(self):
        entries = dict()
        events = self.__events_repository.read_all()
        for filename in listdir(self._path):
            json_name = splitext(filename)[0]
            if json_name != 'metadata':
                try:
                    ticket_id = int(json_name)
                    json_file = JsonFile(self._path, filename)
                    content = json_file.read_all()
                    event = events[content['event_id']]
                    entries[ticket_id] = self.__dict_to_ticket(ticket_id, content,  event)
                except ValueError:
                    raise ValueError(f'Incorrect file {filename} in events storage')

        return entries

    def update(self, ticket: Ticket):
        self.create(ticket)

    def delete(self, ticket_id: int):
        file_path = self._path.joinpath(f'{ticket_id}.json')
        if file_path.exists():
            remove(file_path)

    @staticmethod
    def __dict_to_ticket(ticket_id: int, content: dict, event: Event):
        return Ticket.of(
            ticket_id,
            event,
            content['name'],
            datetime.fromisoformat(content['date']),
            content['is_student']
        )

    @staticmethod
    def __ticket_to_dict(ticket: Ticket):
        return {
            'event_id': ticket.event.id,
            'name': ticket.name,
            'date': ticket.date.isoformat(),
            'is_student': ticket.is_student
        }
