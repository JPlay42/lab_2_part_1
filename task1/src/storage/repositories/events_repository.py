from datetime import datetime
from os import remove

from task1.src.storage.entities.event import Event
from task1.src.storage.json_file import JsonFile
from task1.src.storage.repositories.repository import Repository


class EventsRepository(Repository):
    def __init__(self):
        super().__init__('events')

    def create(self, event: Event):
        ids = super()._get_existing_ids()
        if event.id is None:
            event_id = self._new_entry_id()
        else:
            event_id = event.id
        file = JsonFile(self._path, str(event_id))
        file.write_all(self.__event_to_dict(event))
        return event_id

    def read(self, event_id: int):
        json_file = JsonFile(self._path, str(event_id))
        content = json_file.read_all()
        return self.__dict_to_event(event_id, content)

    def read_all(self):
        entries = dict()
        for event_id in super()._get_existing_ids():
            json_file = JsonFile(self._path, f'{event_id}.json')
            content = json_file.read_all()
            entries[event_id] = self.__dict_to_event(event_id, content)

        return entries

    def update(self, event: Event):
        self.create(event)

    def delete(self, event_id: int):
        file_path = self._path.joinpath(f'{event_id}.json')
        if file_path.exists():
            remove(file_path)

    def __write(self, event: Event):
        if event.id is None:
            event_id = self._new_entry_id()
        else:
            event_id = event.id
        file = JsonFile(self._path, str(event_id))
        file.write_all(self.__event_to_dict(event))
        return event_id

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
