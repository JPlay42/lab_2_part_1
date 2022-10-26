import unittest
from datetime import datetime

from ex1 import Ticket, LateTicket, AdvanceTicket, StudentTicket


class MyTestCase(unittest.TestCase):
    def test_constructor_validation(self):
        with self.assertRaises(TypeError):
            Ticket('not a number')
        with self.assertRaises(ValueError):
            Ticket(-42)

    def test_factory_method_validation(self):
        with self.assertRaises(TypeError):
            Ticket.of('not a number', datetime(2022, 1, 1))
        with self.assertRaises(TypeError):
            Ticket.of(1, 'not a datetime')
        with self.assertRaises(TypeError):
            Ticket.of(1, datetime(2022, 1, 1), 'not a bool')
        with self.assertRaises(ValueError):
            Ticket.of(0, datetime(2022, 1, 1))
        with self.assertRaises(ValueError):
            Ticket.of(1, datetime(2077, 26, 12))

    def test_number(self):
        ticket = Ticket(1)
        self.assertEqual(1, ticket.number)

    def test_regular_ticket(self):
        ticket = Ticket.of(1, datetime(2022, 10, 10))
        self.assertIsInstance(ticket, Ticket)
        self.assertEqual(300, ticket.price)

    def test_late_ticket(self):
        ticket = Ticket.of(2, datetime(2022, 11, 10))
        self.assertIsInstance(ticket, LateTicket)
        self.assertEqual(330, ticket.price)

    def test_advance_ticket(self):
        ticket = Ticket.of(3, datetime(2022, 1, 1))
        self.assertIsInstance(ticket, AdvanceTicket)
        self.assertEqual(180, ticket.price)

    def test_student_ticket(self):
        ticket = Ticket.of(4, datetime(2022, 10, 10), True)
        self.assertIsInstance(ticket, StudentTicket)
        self.assertEqual(150, ticket.price)


if __name__ == '__main__':
    unittest.main()
