from os import listdir, remove

from task1.src.storage.entities.event import Event
from task1.src.storage.json_file import JsonFile
from task1.src.storage.repositories.repository import Repository


class EventsRepository(Repository):
    def __init__(self):
        super().__init__('events')

    def create(self, event: Event):
        self.update(self._new_entry_id(), event)

    def read(self, event_id: int):
        json_file = JsonFile(self._path, str(event_id))
        content = json_file.read_all()
        return self.__dict_to_event(content)

    def read_all(self):
        entries = list()
        for filename in listdir(self._path):
            json_file = JsonFile(self._path, filename)
            content = json_file.read_all()
            entries.append(self.__dict_to_event(content))
        return entries

    def update(self, event_id: int, event: Event):
        file = JsonFile(self._path, str(event_id))
        file.write_all(self.__event_to_dict(event))

    def delete(self, event_id: int):
        file_path = self._path.joinpath(f'{event_id}.json')
        if file_path.exists():
            remove(file_path)

    @staticmethod
    def __dict_to_event(content: dict):
        return Event(
            content['name'],
            content['date'],
            content['price']
        )

    @staticmethod
    def __event_to_dict(event: Event):
        return {
            'name': event.name,
            'date': event.date,
            'price': event.price
        }
