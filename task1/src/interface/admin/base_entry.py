from abc import ABC, abstractmethod

from task1.src.interface.interface import Interface
from task1.src.storage.repositories.repository import Repository


class BaseEntryAdminInterface(Interface, ABC):
    def __init__(self, repo: Repository):
        self._repo = repo

    def run(self):
        print('Select an action: ')
        print('1) Create new entry with auto-generated ID')
        print('2) Create new entry with custom ID')
        print('3) Read entry by ID')
        print('4) Read all entries')
        print('5) Update existing entry')
        print('6) Delete entry')
        match self._input_options(6):
            case 1:
                self._create()
            case 2:
                self._create_with_id()
            case 3:
                self._read()
            case 4:
                self._read_all()
            case 5:
                self._update()
            case 6:
                self._delete()

    def _create(self):
        self._common_create(None)

    def _create_with_id(self):
        self._common_create(self._get_entry_id())

    def _read(self):
        print(self._repo.read(self._get_entry_id()))

    def _read_all(self):
        for entry in self._repo.read_all().values():
            print(entry)

    def _update(self):
        try:
            self._repo.update(self._get_entry(self._get_entry_id()))
        except ValueError as e:
            print(e)

    def _delete(self):
        self._repo.delete(self._get_entry_id())

    def _common_create(self, event_id: int | None):
        created_event_id = self._repo.create(self._get_entry(event_id))
        if event_id is None:
            print(f'New entry ID is {created_event_id}')

    @abstractmethod
    def _get_entry(self, entry_id: int):
        pass

    @abstractmethod
    def _get_entry_id(self):
        pass
