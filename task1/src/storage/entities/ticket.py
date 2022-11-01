from abc import abstractmethod, ABC
from dataclasses import dataclass
from datetime import datetime
from types import NoneType

from task1.src.storage.entities.event import Event


@dataclass(frozen=True)
class Ticket(ABC):
    event: Event | None
    name: str
    date: datetime
    is_student: bool

    def __post_init__(self):
        if not isinstance(self.event, (Event, NoneType)):
            raise TypeError('event is not Event')

        if not isinstance(self.name, str):
            raise TypeError('name is not str')
        if self.name == '':
            raise ValueError('name is empty')

        if not isinstance(self.date, datetime):
            raise TypeError('date is not datetime')
        if self.date > self.event.date:
            raise ValueError('ticket is bought after event is started')

        if not isinstance(self.is_student, bool):
            raise TypeError('is_student is not bool')

    @staticmethod
    def of(event: Event, name: str, date: datetime, is_student: bool):
        days_to_event = (event.date - date).days
        if days_to_event >= 60:
            return AdvanceTicket(event, name, date, is_student)
        if days_to_event < 10:
            return LateTicket(event, name, date, is_student)
        return RegularTicket(event, name, date, is_student)

    @abstractmethod
    def price(self):
        pass


class AdvanceTicket(Ticket):
    def price(self):
        price = self.event.price
        if self.is_student:
            price *= 0.5
        else:
            price *= 0.6
        return int(price)


class LateTicket(Ticket):
    def price(self):
        price = self.event.price * 1.1
        if self.is_student:
            price *= 0.5
        return int(price)


class RegularTicket(Ticket):
    def price(self):
        price = self.event.price
        if self.is_student:
            price *= 0.5
        return int(price)
