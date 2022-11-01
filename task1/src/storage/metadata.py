from pathlib import Path

from task1.src.storage.json_file import JsonFile


class Metadata(JsonFile):
    def __init__(self, folder: Path):
        super().__init__(folder, 'metadata')
        self.write('entries_count', 0)

    def new_entry_id(self):
        return self.increment_and_get('entries_count')
