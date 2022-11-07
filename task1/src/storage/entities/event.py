from dataclasses import dataclass
from datetime import datetime
from types import NoneType


@dataclass(frozen=True)
class Event:
    id: int | None
    name: str
    date: datetime
    price: int

    def __post_init__(self):
        if not isinstance(self.id, (int, NoneType)):
            raise TypeError('id is not int')
        if self.id is not None and self.id <= 0:
            raise ValueError('id is not positive')

        if not isinstance(self.name, str):
            raise TypeError('name is not str')
        if self.name == '':
            raise ValueError('name is empty')

        if not isinstance(self.date, datetime):
            raise TypeError('date is not datetime')

        if not isinstance(self.price, int):
            raise TypeError('price is not int')
        if self.price < 0:
            raise ValueError('price is smaller than 0')

    def is_in_the_future(self):
        return self.date > datetime.now()

