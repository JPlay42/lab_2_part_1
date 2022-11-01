from task1.src.storage.repositories.repository import Repository


class TicketsRepository(Repository):
    def __init__(self):
        super().__init__('tickets')
