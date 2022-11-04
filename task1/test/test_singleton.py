import unittest

from task1.src.singleton import Singleton


class TestSingleton1(Singleton):
    pass


class TestSingleton2(Singleton):
    pass


class SingletonTest(unittest.TestCase):
    def test_single_init_same_types(self):
        singleton1 = TestSingleton1()
        another_singleton1 = TestSingleton1()
        self.assertEqual(id(singleton1), id(another_singleton1))

    def test_diff_init_diff_types(self):
        singleton1 = TestSingleton1()
        singleton2 = TestSingleton2()
        self.assertNotEqual(id(singleton1), id(singleton2))


if __name__ == '__main__':
    unittest.main()
