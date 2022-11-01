from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Event:
    name: str
    date: datetime
    price: int

    def __post_init__(self):
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

