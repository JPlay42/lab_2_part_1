from datetime import datetime
from os import remove

from task1.src.storage.entities.event import Event
from task1.src.storage.json_file import JsonFile
from task1.src.storage.repositories.repository import Repository


class EventsRepository(Repository[Event]):
    def __init__(self):
        super().__init__('events')

    def create(self, event: Event):
        if event.id is None:
            event_id = self.generate_id()
        elif not self.add_custom_id(event.id):
            raise ValueError(f'Event with id {event.id} already exists')
        else:
            event_id = event.id
        self.__write(event, event_id)
        return event_id

    def read(self, event_id: int):
        json_file = JsonFile(self._path, str(event_id))
        content = json_file.read_all()
        return self.__dict_to_event(event_id, content)

    def read_all(self):
        entries = dict()
        for event_id in super().get_existing_ids():
            json_file = JsonFile(self._path, f'{event_id}.json')
            content = json_file.read_all()
            entries[event_id] = self.__dict_to_event(event_id, content)

        return entries

    def update(self, event: Event):
        if event.id is None:
            raise ValueError('Event id is None, nothing to update')
        existing_ids = self.get_existing_ids()
        if event.id not in existing_ids:
            raise ValueError(f'Event with id {event.id} does not exist')
        self.__write(event, event.id)

    def delete(self, event_id: int):
        existing_ids = super().get_existing_ids()
        if event_id in existing_ids:
            file_path = self._path.joinpath(f'{event_id}.json')
            super().delete_id(event_id)
            remove(file_path)
        else:
            raise ValueError(f'Event with id {event_id} does not exist')

    def __write(self, event: Event, event_id: int):
        file = JsonFile(self._path, str(event_id))
        file.write_all(self.__event_to_dict(event))

    @staticmethod
    def __dict_to_event(event_id: int, content: dict):
        return Event(
            event_id,
            content['name'],
            datetime.fromisoformat(content['date']),
            content['price']
        )

    @staticmethod
    def __event_to_dict(event: Event):
        return {
            'name': event.name,
            'date': event.date.isoformat(),
            'price': event.price
        }
