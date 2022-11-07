from datetime import datetime

from task1.src.interface.admin.base_entry import BaseEntryAdminInterface
from task1.src.storage import TicketsRepository, EventsRepository
from task1.src.storage.entities.ticket import Ticket


class TicketsAdminInterface(BaseEntryAdminInterface):
    __events_repo = EventsRepository()

    def __init__(self):
        super().__init__(TicketsRepository())

    def _get_entry_id(self):
        return int(input('Ticket ID: '))

    def _get_entry(self, ticket_id: int):
        event = self.__events_repo.read(int(input('Event ID: ')))
        print('Current event is: ')
        print(event)
        name = input('Name: ')
        date = datetime(
            day=int(input('Day: ')),
            month=int(input('Month: ')),
            year=int(input('Year: '))
        )
        is_student = super()._get_boolean(input('Are they student? (yes/no): '))
        return Ticket.of(
            ticket_id,
            event,
            name,
            date,
            is_student
        )
