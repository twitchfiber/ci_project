import math


def my_datetime(num_sec):
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12']

    month_days_standard = {
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

    month_days_leap = {
        '01': 31,
        '02': 29,
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

    year_found = False
    while year_found is False:
        current_year_is_leap = is_leapyear(current_year)
        if current_year_is_leap:
            days_in_year = 366
        else:
            days_in_year = 365
        if num_days > days_in_year:
            num_days -= days_in_year
            current_year += 1
        else:
            year_found = True

    i = 0
    current_year_is_leap = is_leapyear(current_year)
    if current_year_is_leap:
        month_days = month_days_leap
    else:
        month_days = month_days_standard
    while num_days >= month_days[months[i]]:
        num_days -= month_days[months[i]]
        i += 1

    return '-'.join([str(months[i]), (str(math.ceil(num_days)).zfill(2)),
                     str(current_year)])


# Reference: https://en.wikipedia.org/wiki/Leap_year
def is_leapyear(year):
    if type(year) is not int:
        return False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
