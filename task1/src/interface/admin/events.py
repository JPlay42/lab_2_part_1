from datetime import datetime

from task1.src.interface.interface import Interface
from task1.src.storage import EventsRepository
from task1.src.storage.entities.event import Event


class EventsAdminInterface(Interface):
    __events_repo = EventsRepository()

    def run(self):
        print('Select an action: ')
        print('1) Create new event with auto-generated ID')
        print('2) Create new event with custom ID')
        print('3) Read event by ID')
        print('4) Read all events')
        print('5) Update existing event')
        print('6) Delete event')
        match self._input_options(6):
            case 1:
                self.create()
            case 2:
                self.create_with_id()
            case 3:
                self.read()
            case 4:
                self.read_all()
            case 5:
                self.update()
            case 6:
                self.delete()

    def create(self):
        self.__common_create(None)

    def create_with_id(self):
        self.__common_create(self.__get_event_id())

    def read(self):
        print(self.__events_repo.read(self.__get_event_id()))

    def read_all(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def __common_create(self, event_id: int | None):
        name = input('Name: ')
        date = datetime(
            day=int(input('Day: ')),
            month=int(input('Month: ')),
            year=int(input('Year: '))
        )
        price = int(input('Price: '))
        event = Event(
            event_id,
            name,
            date,
            price
        )
        created_event_id = self.__events_repo.create(event)
        if event_id is None:
            print(f'New event ID is {created_event_id}')

    @staticmethod
    def __get_event_id():
        return int(input('Event ID: '))