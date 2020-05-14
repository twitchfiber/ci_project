import math


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

    # DEBUG STATEMENTS
    # print('current year', current_year)
    # print('num days left', num_days)
    # print('month(i)', months[i])
    # print('num days', math.ceil(num_days))

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
