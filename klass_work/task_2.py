import random
import sys


__all__ = ['function_1']
def function_1(lower_limit=int(input('Введите низ')), upper_limit=int(input('Введите верх')), number_of_attempts=int(input('Введитк кол-во попыток'))):
    num = random.randint(lower_limit, upper_limit)
    while True:
        answer = int(input("Введите число:"))
        if answer < num:
            print("Загаданное число больше")
            number_of_attempts -= 1
        elif answer > num:
            print("Загаданное число меньше")
            number_of_attempts -= 1
        else:
            return True
        if number_of_attempts == 0:
            return False



print(function_1(*(int(i) for i in sys.argv[1:])))