from pathlib import Path

from task1.src.storage.json_file import JsonFile


class Metadata(JsonFile):
    def __init__(self, folder: Path):
        super().__init__(folder, 'metadata')

    def generate_id(self):
        content = self.read_all()
        new_id = content['last_generated_id'] + 1
        custom_ids = content['custom_ids']
        while new_id in custom_ids:
            new_id += 1
        self.write('last_generated_id', new_id)
        return new_id

    def add_custom_id(self, new_id: int):
        content = self.read_all()
        if new_id <= content['last_generated_id']:
            return False
        custom_ids: list = content['custom_ids']
        if new_id in custom_ids:
            return False
        custom_ids.append(new_id)
        self.write('custom_ids', custom_ids)
        return True

    def delete_id(self, id_to_delete: int):
        deleted_ids: list = self.read('deleted_ids')
        if id_to_delete not in deleted_ids:
            deleted_ids.append(id_to_delete)
        self.write('deleted_ids', deleted_ids)

    def get_existing_ids(self):
        content = self.read_all()
        last_generated_id = content['last_generated_id']
        custom_ids = content['custom_ids']
        deleted_ids = content['deleted_ids']
        existing_ids = list()

        for i in range(1, last_generated_id + 1):
            if i not in deleted_ids:
                existing_ids.append(i)

        for i in custom_ids:
            if i > last_generated_id and i not in deleted_ids:
                existing_ids.append(i)

        return existing_ids

    def _post_create(self):
        initial_data = {
            'last_generated_id': 0,
            'custom_ids': list(),
            # performance optimization, we don't look up files in filesystem
            'deleted_ids': list()
        }
        self.write_all(initial_data)
