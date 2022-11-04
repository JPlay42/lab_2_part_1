import unittest
from datetime import datetime

from task1.src.storage.entities.event import Event


class EventTest(unittest.TestCase):
    def test_getters(self):
        now = datetime.now()
        event = Event(1, 'name', now, 300)
        self.assertEqual(1, event.id)
        self.assertEqual('name', event.name)
        self.assertEqual(now, event.date)
        self.assertEqual(300, event.price)

    def test_validation(self):
        now = datetime.now()
        Event(1, 'name', now, 300)
        Event(None, 'name', now, 300)
        with self.assertRaises(TypeError):
            Event('duck', 'name', now, 300)
        with self.assertRaises(ValueError):
            Event(0, 'name', now, 300)
        with self.assertRaises(TypeError):
            Event(1, 123, now, 300)
        with self.assertRaises(ValueError):
            Event(1, '', now, 300)
        with self.assertRaises(TypeError):
            Event(1, 'name', 'not datetime', 300)
        with self.assertRaises(TypeError):
            Event(1, 'name', now, 'not int')
        with self.assertRaises(ValueError):
            Event(1, 'name', now, -1)


if __name__ == '__main__':
    unittest.main()
