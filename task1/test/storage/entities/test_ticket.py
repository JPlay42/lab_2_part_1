import unittest
from datetime import datetime, timedelta

from task1.src.storage.entities.event import Event
from task1.src.storage.entities.ticket import Ticket, RegularTicket, AdvanceTicket, LateTicket


class TicketTest(unittest.TestCase):
    def test_validation(self):
        now = datetime.now() + timedelta(days=5)
        month_before = now - timedelta(days=30)
        event = Event(1, 'Event name', now, 300)

        RegularTicket(1, event, 'Ivan Kuruch', month_before, True)
        RegularTicket(None, event, 'Ivan Kuruch', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket('not id', event, 'Ivan Kuruch', month_before, True)
        with self.assertRaises(ValueError):
            RegularTicket(0, event, 'Ivan Kuruch', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket(1, 'not event', 'Ivan Kuruch', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket(1, event, 123, month_before, True)
        with self.assertRaises(ValueError):
            RegularTicket(1, event, '', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket(1, event, 'Ivan Kuruch', 'not datetime', True)
        with self.assertRaises(ValueError):
            RegularTicket(1, event, 'Ivan Kuruch', now + timedelta(days=1), True)
        with self.assertRaises(TypeError):
            RegularTicket(1, event, 'Ivan Kuruch', month_before, 'not bool')

    def test_factory_method(self):
        now = datetime.now() + timedelta(days=5)
        event = Event(1, 'Google HashCode', now, 300)

        self.assertIsInstance(
            Ticket.of(1, event, 'Ivan Kuruch', now - timedelta(days=30), True),
            RegularTicket
        )
        self.assertIsInstance(
            Ticket.of(1, event, 'Ivan Kuruch', now - timedelta(days=60), True),
            AdvanceTicket
        )
        self.assertIsInstance(
            Ticket.of(1, event, 'Ivan Kuruch', now - timedelta(days=9), True),
            LateTicket
        )

    def test_regular_ticket_price(self):
        event_time = datetime.now() + timedelta(days=5)
        ticket_purchase_time = event_time - timedelta(days=30)
        event = Event(1, 'Test event', event_time, 100)

        ticket = Ticket.of(1, event, 'Jack Daniels', ticket_purchase_time, False)
        self.assertEqual(100, ticket.price())

        ticket = Ticket.of(1, event, 'Mykola Pylypchuk', ticket_purchase_time, True)
        self.assertEqual(50, ticket.price())

    def test_late_ticket_price(self):
        event_time = datetime.now() + timedelta(days=5)
        ticket_purchase_time = event_time - timedelta(days=7)
        event = Event(1, 'Test event', event_time, 100)

        ticket = Ticket.of(1, event, 'Jack Daniels', ticket_purchase_time, False)
        self.assertEqual(110, ticket.price())

        ticket = Ticket.of(1, event, 'Mykola Pylypchuk', ticket_purchase_time, True)
        self.assertEqual(55, ticket.price())

    def test_advance_ticket_price(self):
        event_time = datetime.now() + timedelta(days=5)
        ticket_purchase_time = event_time - timedelta(days=60)
        event = Event(1, 'Test event', event_time, 100)

        ticket = Ticket.of(1, event, 'Jack Daniels', ticket_purchase_time, False)
        self.assertEqual(60, ticket.price())

        ticket = Ticket.of(1, event, 'Mykola Pylypchuk', ticket_purchase_time, True)
        self.assertEqual(50, ticket.price())


if __name__ == '__main__':
    unittest.main()
