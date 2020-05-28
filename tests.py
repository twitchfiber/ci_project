import unittest
from task import is_leapyear, my_datetime, conv_num, conv_endian


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

    def test_time6(self):
        time = 10
        expected = '01-01-1970'
        self.assertEqual(my_datetime(time), expected)

    def test_time7(self):
        time = 86399
        expected = '01-01-1970'
        self.assertEqual(my_datetime(time), expected)

    def test_time8(self):
        time = 86401
        expected = '01-02-1970'
        self.assertEqual(my_datetime(time), expected)

    def test_time9(self):
        time = 347080258
        expected = '12-31-1980'
        self.assertEqual(my_datetime(time), expected)

    def test_time10(self):
        time = 347166658
        expected = '01-01-1981'
        self.assertEqual(my_datetime(time), expected)

    def test_time11(self):
        time = 1582945858
        expected = '02-29-2020'
        self.assertEqual(my_datetime(time), expected)

    def test_time12(self):
        time = 1583032258
        expected = '03-01-2020'
        self.assertEqual(my_datetime(time), expected)

    def test_time13(self):
        time = 1582859458
        expected = '02-28-2020'
        self.assertEqual(my_datetime(time), expected)

    def test_time14(self):
        time = 883527358
        expected = '12-31-1997'
        self.assertEqual(my_datetime(time), expected)

    def test_time15(self):
        time = 883613758
        expected = '01-01-1998'
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

    def test_conv_num9(self):
        num_str = '-123.'
        expected = -123.0
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num10(self):
        num_str = '-.45'
        expected = -0.45
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num11(self):
        num_str = '-.45'
        expected = -0.45
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num12(self):
        num_str = '-123.45'
        expected = -123.45
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num13(self):
        num_str = '0xAD4'
        expected = 2772
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num14(self):
        num_str = '-0xAD4'
        expected = -2772
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num15(self):
        num_str = 'hello'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num16(self):
        num_str = '-0xad4'
        expected = -2772
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num17(self):
        num_str = '1FF'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num18(self):
        num_str = ''
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_num19(self):
        num_str = [1, 2, 3]
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_conv_endian1(self):
        num = 954786
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num), expected)

    def test_conv_endian2(self):
        num = 954786
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num, 'big'), expected)

    def test_conv_endian3(self):
        num = 954786
        expected = 'A2 91 0E'
        self.assertEqual(conv_endian(num, 'little'), expected)

    def test_conv_endian4(self):
        num = 954786
        expected = None
        self.assertEqual(conv_endian(num, 'hello'), expected)

    def test_conv_endian5(self):
        num = -954786
        expected = '-0E 91 A2'
        self.assertEqual(conv_endian(num), expected)

    def test_conv_endian6(self):
        num = -954786
        expected = '-A2 91 0E'
        self.assertEqual(conv_endian(num, 'little'), expected)

    def test_conv_endian7(self):
        num = 0
        expected = '00'
        self.assertEqual(conv_endian(num, 'little'), expected)

    def test_conv_endian8(self):
        num = 0
        expected = '00'
        self.assertEqual(conv_endian(num, 'big'), expected)

    def test_conv_endian9(self):
        num = 0
        expected = '00'
        self.assertEqual(conv_endian(num), expected)

    def test_conv_endian10(self):
        num = 87
        expected = '57'
        self.assertEqual(conv_endian(num, 'little'), expected)

    def test_conv_endian11(self):
        num = 87
        expected = '57'
        self.assertEqual(conv_endian(num, 'big'), expected)

    def test_conv_endian12(self):
        num = 87
        expected = '57'
        self.assertEqual(conv_endian(num), expected)


if __name__ == '__main__':
    unittest.main()
