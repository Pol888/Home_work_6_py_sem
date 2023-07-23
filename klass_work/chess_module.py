import random

__all__ = ['random_placement', 'queens_8']


def random_placement():
    a = ['1', '2', '3', '4', '5', '6', '7', '8']
    b = ['1', '2', '3', '4', '5', '6', '7', '8']
    random.shuffle(a)
    random.shuffle(b)
    for i, j in zip(a, b):
        yield i + ':' + j


def queens_8(c: list):
    for num, i in enumerate(c):
        check_list = c[0:num] + c[num + 1:len(c)]
        for j in check_list:
            if i[0] == j[0] or i[2] == j[2]:
                return False
            else:
                count = 1
                flag = True
                while flag:
                    if int(i[0]) + count <= 8 and int(i[2]) + count <= 8:
                        check_t = f'{int(i[0]) + count}:{int(i[2]) + count}'
                        if check_t in check_list:
                            return False
                    if int(i[0]) + count <= 8 and int(i[2]) - count >= 1:
                        check_t = f'{int(i[0]) + count}:{int(i[2]) - count}'
                        if check_t in check_list:
                            return False
                    if int(i[0]) - count >= 1 and int(i[2]) + count <= 8:
                        check_t = f'{int(i[0]) - count}:{int(i[2]) + count}'
                        if check_t in check_list:
                            return False
                    if int(i[0]) - count >= 1 and int(i[2]) - count >= 1:
                        check_t = f'{int(i[0]) - count}:{int(i[2]) - count}'
                        if check_t in check_list:
                            return False

                    count += 1
                    if count == 9:
                        flag = False
    return True


def main():
    count = 0
    flag = True
    while flag:
        gen = list(random_placement())
        if queens_8(gen):
            count += 1
            print(*gen)
        if count == 4:
            flag = False


'''%7:4 3:2 1:3 4:8 2:7 6:1 5:5 8:6%
   
   %8:7 5:6 3:5 4:8 2:2 6:1 7:3 1:4%
   
   %1:3 8:5 3:8 5:4 4:2 7:7 2:6 6:1%
   
   %1:7 5:6 7:3 8:5 2:4 3:2 6:1 4:8%'''

if __name__ == '__main__':
    main()
