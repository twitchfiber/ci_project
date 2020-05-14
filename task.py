def my_datetime(num_sec):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Leap year: 29, Non-Leap: 28
    month_days = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31
    }


# Reference: https://en.wikipedia.org/wiki/Leap_year
def is_leapyear(year):
    if type(year) is not int:
        return False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
