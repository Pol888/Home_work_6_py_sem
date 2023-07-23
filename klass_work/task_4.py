import random


__all__ = ['p', 'function_riddle', 'for_f']
def function_riddle(mystery, guess_options, number_of_attempts):

    count = 0
    guess_options = list(map(str, guess_options))
    correct_answer = guess_options[0]
    random.shuffle(guess_options)
    print(f"Загадка: {mystery}\n")
    while True:
        print(f'Варианты ответов:{guess_options}\n')
        answer = input('Введите ответ\n')
        if answer == correct_answer:
            f_analysis(mystery, count + 1)
            return count + 1
        else:
            count += 1
            if count == number_of_attempts:
                return 0
            else:
                print('не правильно')
                continue

def for_f(dict_d: dict):
    for key, val in dict_d.items():

        print(function_riddle(key, val, int(input('кол-во попыток..'))))


__dict_f = {}


def f_analysis(strng, count):
    f_analysis.__dict__['c'] = f_analysis.__dict__['c'] + 1
    __dict_f[strng + str(f_analysis.__dict__['c'])] = count


def p(d: dict):
    for k, v in d.items():
        print(k, v)



f_analysis.__dict__['c'] = 0
for_f({'mm': [1, 2, 3], 'vv': [3, 5, 7]})
p(__dict_f)



