import unittest
from task import is_leapyear, my_datetime, conv_num


class TestCase(unittest.TestCase):

    def test_time1(self):
        time = 0
        expected = '01-01-1970'
        self.assertEqual(my_datetime(time), expected)

    def test_time2(self):
        time = 123456789
        expected = '11-29-1973'
        self.assertEqual(my_datetime(time), expected)

    def test_time3(self):
        time = 9876543210
        expected = '12-22-2282'
        self.assertEqual(my_datetime(time), expected)

    def test_time4(self):
        time = 1589429599
        expected = '05-14-2020'
        self.assertEqual(my_datetime(time), expected)

    def test_time5(self):
        time = 1232353451
        expected = '01-19-2009'
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

    def test_conv_num1(self):
        num_str = '12345'
        expected = 12345
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num2(self):
        num_str = '0xAZ4'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num3(self):
        num_str = '12345A'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num4(self):
        num_str = '12.3.45'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num5(self):
        num_str = '123.'
        expected = 123.0
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num6(self):
        num_str = '.45'
        expected = 0.45
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num7(self):
        num_str = '.45123440'
        expected = 0.45123440
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num8(self):
        num_str = '123.45'
        expected = 123.45
        self.assertEqual(conv_num(num_str), expected)



if __name__ == '__main__':
    unittest.main()
