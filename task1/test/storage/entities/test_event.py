import unittest
from datetime import datetime

from task1.src.storage.entities.event import Event


class EventTest(unittest.TestCase):
    def test_getters(self):
        now = datetime.now()
        event = Event('name', now, 300)
        self.assertEqual('name', event.name)
        self.assertEqual(now, event.date)
        self.assertEqual(300, event.price)

    def test_validation(self):
        now = datetime.now()
        with self.assertRaises(TypeError):
            Event(123, now, 300)
        with self.assertRaises(ValueError):
            Event('', now, 300)
        with self.assertRaises(TypeError):
            Event('name', 'not datetime', 300)
        with self.assertRaises(TypeError):
            Event('name', now, 'not int')
        with self.assertRaises(ValueError):
            Event('name', now, -1)


if __name__ == '__main__':
    unittest.main()