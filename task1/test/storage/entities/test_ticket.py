import unittest
from datetime import datetime, timedelta

from task1.src.storage.entities.event import Event
from task1.src.storage.entities.ticket import Ticket, RegularTicket, AdvanceTicket, LateTicket


class TicketTest(unittest.TestCase):
    def test_validation(self):
        now = datetime.now()
        month_before = now - timedelta(days=30)
        event = Event('Event name', now, 300)

        RegularTicket(event, 'Ivan Kuruch', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket('not event', 'Ivan Kuruch', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket(event, 123, month_before, True)
        with self.assertRaises(ValueError):
            RegularTicket(event, '', month_before, True)
        with self.assertRaises(TypeError):
            RegularTicket(event, 'Ivan Kuruch', 'not datetime', True)
        with self.assertRaises(ValueError):
            RegularTicket(event, 'Ivan Kuruch', now + timedelta(days=1), True)
        with self.assertRaises(TypeError):
            RegularTicket(event, 'Ivan Kuruch', month_before, 'not bool')

    def test_factory_method(self):
        now = datetime.now()
        event = Event('Google HashCode', now, 300)

        self.assertIsInstance(
            Ticket.of(event, 'Ivan Kuruch', now - timedelta(days=30), True),
            RegularTicket
        )
        self.assertIsInstance(
            Ticket.of(event, 'Ivan Kuruch', now - timedelta(days=60), True),
            AdvanceTicket
        )
        self.assertIsInstance(
            Ticket.of(event, 'Ivan Kuruch', now - timedelta(days=9), True),
            LateTicket
        )

    def test_regular_ticket_price(self):
        event_time = datetime.now()
        ticket_purchase_time = event_time - timedelta(days=30)
        event = Event('Test event', event_time, 100)

        ticket = Ticket.of(event, 'Jack Daniels', ticket_purchase_time, False)
        self.assertEqual(100, ticket.price())

        ticket = Ticket.of(event, 'Mykola Pylypchuk', ticket_purchase_time, True)
        self.assertEqual(50, ticket.price())

    def test_late_ticket_price(self):
        event_time = datetime.now()
        ticket_purchase_time = event_time - timedelta(days=7)
        event = Event('Test event', event_time, 100)

        ticket = Ticket.of(event, 'Jack Daniels', ticket_purchase_time, False)
        self.assertEqual(110, ticket.price())

        ticket = Ticket.of(event, 'Mykola Pylypchuk', ticket_purchase_time, True)
        self.assertEqual(55, ticket.price())

    def test_advance_ticket_price(self):
        event_time = datetime.now()
        ticket_purchase_time = event_time - timedelta(days=60)
        event = Event('Test event', event_time, 100)

        ticket = Ticket.of(event, 'Jack Daniels', ticket_purchase_time, False)
        self.assertEqual(60, ticket.price())

        ticket = Ticket.of(event, 'Mykola Pylypchuk', ticket_purchase_time, True)
        self.assertEqual(50, ticket.price())


if __name__ == '__main__':
    unittest.main()
