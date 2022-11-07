from datetime import datetime

from task1.src.interface.admin.base_entry import BaseEntryAdminInterface
from task1.src.storage import EventsRepository
from task1.src.storage.entities.event import Event


class EventsAdminInterface(BaseEntryAdminInterface):

    def __init__(self):
        super().__init__(EventsRepository())

    def _get_entry(self, event_id: int):
        name = input('Name: ')
        date = datetime(
            day=int(input('Day: ')),
            month=int(input('Month: ')),
            year=int(input('Year: '))
        )
        price = int(input('Price: '))
        return Event(
            event_id,
            name,
            date,
            price
        )

    def _get_entry_id(self):
        return int(input('Event ID: '))
