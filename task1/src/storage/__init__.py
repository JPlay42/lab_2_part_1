from pathlib import Path

from task1.src.storage.repositories.events import EventsRepository
from task1.src.storage.repositories.tickets import TicketsRepository

Path('../storage').mkdir(exist_ok=True)

events_repo = EventsRepository()
tickets_repo = TicketsRepository()
