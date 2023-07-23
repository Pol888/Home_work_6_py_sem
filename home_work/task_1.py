import sys


def date_check(date):
    dd, mm, yyyy = date.split('.')
    days = [31, definition_of_leap_year(yyyy), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 9999 >= int(yyyy) >= 1 and 12 >= int(mm) >= 1:
        if 1 <= int(dd) <= days[int(mm) - 1]:
            return True
    return False


def definition_of_leap_year(yyyy):
    yyyy = int(yyyy)
    if yyyy % 4 == 0:
        if yyyy % 100 != 0:
            return 29
        else:
            if yyyy % 400 == 0:
                return 29
            else:
                return 28
    else:
        return 28


def main():
    if len(sys.argv) == 2:
        print(date_check(sys.argv[1]))
    elif len(sys.argv) == 1:
        print(date_check(input('Введите дату в формате %dd.mm.yyyy%')))


if __name__ == '__main__':
    main()
