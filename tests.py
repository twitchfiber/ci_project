import unittest
from task import is_leapyear, my_datetime


class TestCase(unittest.TestCase):

    def test_time1(self):
        time = 0
        expected = '01-01-1970'
        self.assertEqual(my_datetime(time), expected)

    def test_time2(self):
        time = 123456789
        expected = '11-29-1973'
        self.assertEqual(my_datetime(time), expected)

    def test_leap1(self):
        year = 1972
        expected = True
        self.assertEqual(is_leapyear(year), expected)

    def test_leap2(self):
        year = 1970
        expected = False
        self.assertEqual(is_leapyear(year), expected)

    def test_leap3(self):
        year = 2020
        expected = True
        self.assertEqual(is_leapyear(year), expected)

    def test_leap4(self):
        year = 2022
        expected = False
        self.assertEqual(is_leapyear(year), expected)

    def test_leap5(self):
        year = None
        expected = False
        self.assertEqual(is_leapyear(year), expected)

    def test_leap6(self):
        year = ''
        expected = False
        self.assertEqual(is_leapyear(year), expected)

        
if __name__ == '__main__':
    unittest.main()
