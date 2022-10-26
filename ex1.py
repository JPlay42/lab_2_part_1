from datetime import datetime


class Ticket:
    _initial_price = 300
    _event_date = datetime(2022, 11, 11)

    def __init__(self, number: int):
        if not isinstance(number, int):
            raise TypeError('number is not int')
        if number <= 0:
            raise ValueError('number is not positive')
        self._number = number

    @staticmethod
    def of(number: int, purchase_date: datetime, is_student: bool = False):
        if not isinstance(purchase_date, datetime):
            raise TypeError('purchase_date should be datetime')
        if purchase_date >= Ticket._event_date:
            raise ValueError('Cannot buy a ticket for started event')
        if not isinstance(is_student, bool):
            raise TypeError('is_student should be bool')

        if is_student:
            return StudentTicket(number)

        days_before_event = (Ticket._event_date - purchase_date).days
        if days_before_event >= 60:
            return AdvanceTicket(number)
        if days_before_event < 10:
            return LateTicket(number)

        return Ticket(number)

    def __str__(self):
        return f'Ticket [' \
                   f'number={self._number}; ' \
                   f'initial_price={self._initial_price}; ' \
                   f'event_date={self._event_date}' \
               f']'

    @property
    def number(self):
        return self._number

    @property
    def price(self):
        return self._initial_price


class AdvanceTicket(Ticket):
    @property
    def price(self):
        return int(self._initial_price * 0.6)

    def __str__(self):
        return f'AdvanceTicket [' \
                   f'number={self._number}; ' \
                   f'initial_price={self._initial_price}; ' \
                   f'event_date={self._event_date}' \
               f']'


class StudentTicket(Ticket):
    @property
    def price(self):
        return int(self._initial_price * 0.5)

    def __str__(self):
        return f'StudentTicket [' \
                   f'number={self._number}; ' \
                   f'initial_price={self._initial_price}; ' \
                   f'event_date={self._event_date}' \
               f']'


class LateTicket(Ticket):
    @property
    def price(self):
        return int(self._initial_price * 1.1)

    def __str__(self):
        return f'Ticket [' \
                   f'number={self._number}; ' \
                   f'initial_price={self._initial_price}; ' \
                   f'event_date={self._event_date}' \
               f']'


if __name__ == '__main__':
    ticket = Ticket.of(1, datetime(2022, 11, 10))
    print(ticket.price)
    print(ticket)
