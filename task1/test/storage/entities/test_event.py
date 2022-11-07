import unittest
from datetime import datetime, timedelta

from task1.src.storage.entities.event import Event


class EventTest(unittest.TestCase):
    def test_getters(self):
        now = datetime.now() + timedelta(days=14)
        event = Event(1, 'name', now, 300)
        self.assertEqual(1, event.id)
        self.assertEqual('name', event.name)
        self.assertEqual(now, event.date)
        self.assertEqual(300, event.price)

    def test_validation(self):
        future = datetime.now() + timedelta(days=14)
        Event(1, 'name', future, 300)
        Event(None, 'name', future, 300)
        with self.assertRaises(TypeError):
            Event('duck', 'name', future, 300)
        with self.assertRaises(ValueError):
            Event(0, 'name', future, 300)
        with self.assertRaises(TypeError):
            Event(1, 123, future, 300)
        with self.assertRaises(ValueError):
            Event(1, '', future, 300)
        with self.assertRaises(TypeError):
            Event(1, 'name', 'not datetime', 300)
        with self.assertRaises(TypeError):
            Event(1, 'name', future, 'not int')
        with self.assertRaises(ValueError):
            Event(1, 'name', future, -1)


if __name__ == '__main__':
    unittest.main()
