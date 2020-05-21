import math
import collections

def my_datetime(num_sec):
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12']

    # Leap year: 29, Non-Leap: 28
    month_days = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    if num_sec == 0:
        return '01-01-1970'

    num_days = num_sec / 86400.0

    current_year = 1970
    while num_days >= 365:
        if is_leapyear(current_year):
            num_days -= 366
        else:
            num_days -= 365
        current_year += 1

    i = 0
    current_year_is_leap = is_leapyear(current_year)
    while num_days >= month_days[months[i]]:
        if i == 1 and current_year_is_leap:
            num_days -= 29
        else:
            num_days -= month_days[months[i]]
        i += 1

    return '-'.join([str(months[i]), str(math.ceil(num_days)),
                     str(current_year)])


# Reference: https://en.wikipedia.org/wiki/Leap_year
def is_leapyear(year):
    if type(year) is not int:
        return False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def conv_num(num_str):
    """This function takes in a string and converts it into a base 10 number and returns it"""
    # make string uppercase to make function case agnostic
    upper_num_str = num_str.upper()

    # Start off by checking edge cases
    if invalid_num(upper_num_str):
        return None

    num_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '-': '-'}

    # count valid integers so we can compare with the len(num_str)
    valid_integers = 0
    for char in upper_num_str:
        if char in num_values:
            valid_integers = valid_integers + 1

    # if num_str only contains numbers, call conv_int
    if valid_integers == len(upper_num_str):
        return conv_int(upper_num_str, num_values)

    # if num_str is a floating point with a decimal as the last char
    if upper_num_str[-1] == '.':
        return conv_int(upper_num_str[0:-1], num_values) + 0.0
    # if num_str is a floating point with a decimal as the first char
    elif upper_num_str[0] == '.':
        return 0.0 + conv_float(upper_num_str[1:], num_values)
    # if num_str is a floating point with a -. as the first two chars
    elif upper_num_str[0:2] == '-.':
        return (0.0 + conv_float(upper_num_str[2:], num_values)) * -1
    # if num_str is a floating point that contains a decimal somewhere between the first and last char
    elif '.' in upper_num_str:
        decimal = upper_num_str.split('.')
        left_decimal = decimal[0]
        right_decimal = decimal[1]
        return conv_int(left_decimal, num_values) + conv_float(right_decimal, num_values)
    return 1


def invalid_num(num_str):
    """This helper function takes in the upper case version of num_str and checks for edge cases.
    It returns True if the num_str is invalid.
    """
    count = collections.Counter(num_str)

    # if there is more than 1 decimal then the number is invalid
    if count['.'] > 1:
        return True
    # there can only be at most one X for hexadecimal numbers
    if count['X'] > 1:
        return True
    # empty string
    if len(num_str) == 0:
        return True
    # just hex prefix
    if len(num_str) == 2 and count['0'] == 1 and count['X'] == 1:
        return True
    # just negative sign
    if len(num_str) == 1 and count['-']:
        return True
    # if there are more than 1 negative signs then number is invalid
    if count['-'] > 1:
        return True

    # if number is not hex then there should be no letters
    if count['X'] == 0:
        for char in num_str:
            if char.isalpha():
                return True

    # if number is hex then it should only contain 0X123456789ABCDEF
    valid_hex = '0X123456789ABCDEF'
    if num_str[0:3] == '-0X' or num_str[0:2] == '0X':
        for char in num_str:
            if char not in valid_hex:
                return True
    # if there are no numbers then it is invalid
    num_numbers = 0
    digits = '0123456789'
    for char in num_str:
        if char in digits:
            num_numbers = num_numbers + 1
    if num_numbers < 1:
        return True

    # if we get here then the num_str is valid
    return False


def conv_int(num_str, num_values):
    """This helper function takes in a string containing only numbers and converts
    it into a base 10 number and returns it.
    referenced https://www.geeksforgeeks.org/write-your-own-atoi/
    """
    result = 0
    # initialize the sign to positive
    sign = 1
    start = 0

    # if the first character is negative then update sign
    if num_str[0] == '-':
        sign = -1
        start = 1

    # iterate through num_str and convert to base 10 number
    for i in range(start, len(num_str)):
        result = result * 10 + num_values[num_str[i]]

    # return the number and handle both positive and negative values
    return sign * result


def conv_float(num_str, num_values):
    """This helper function takes in a string containing only numbers that are
    to the right of decimal point and returns a floating point representation of it"""

    result = 0

    for i in range(len(num_str)):
        result = num_values[num_str[i]] / pow(10, i + 1) + result

    return result





