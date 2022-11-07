from datetime import datetime
from os import remove

from task1.src.storage import EventsRepository
from task1.src.storage.entities.event import Event
from task1.src.storage.entities.ticket import Ticket
from task1.src.storage.json_file import JsonFile
from task1.src.storage.repositories.repository import Repository


class TicketsRepository(Repository[Ticket]):
    __events_repository = EventsRepository()

    def __init__(self):
        super().__init__('tickets')

    def create(self, ticket: Ticket):
        if ticket.id is None:
            ticket_id = self.generate_id()
        elif not self.add_custom_id(ticket.id):
            raise ValueError(f'Ticket with id {ticket.id} already exists')
        else:
            ticket_id = ticket.id
        self.__write(ticket, ticket_id)
        return ticket_id

    def read(self, ticket_id: int):
        if ticket_id not in self.get_existing_ids():
            return None
        json_file = JsonFile(self._path, str(ticket_id))
        content = json_file.read_all()
        event = self.__events_repository.read(content['event_id'])
        return self.__dict_to_ticket(ticket_id, content, event)

    def read_all(self):
        entries = dict()
        events = self.__events_repository.read_all()
        for ticket_id in super().get_existing_ids():
            json_file = JsonFile(self._path, f'{ticket_id}.json')
            content = json_file.read_all()
            event = events[content['event_id']]
            entries[ticket_id] = self.__dict_to_ticket(ticket_id, content,  event)

        return entries

    def update(self, ticket: Ticket):
        if ticket.id is None:
            raise ValueError('Ticket id is None, nothing to update')
        existing_ids = self.get_existing_ids()
        if ticket.id not in existing_ids:
            raise ValueError(f'Ticket with id {ticket.id} does not exist')
        self.__write(ticket, ticket.id)

    def delete(self, ticket_id: int):
        existing_ids = super().get_existing_ids()
        if ticket_id in existing_ids:
            file_path = self._path.joinpath(f'{ticket_id}.json')
            super().delete_id(ticket_id)
            remove(file_path)

    def __write(self, ticket: Ticket, ticket_id: int):
        file = JsonFile(self._path, str(ticket_id))
        file.write_all(self.__ticket_to_dict(ticket))

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
