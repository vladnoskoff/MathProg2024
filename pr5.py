import random

array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def game(arr):
    c = 0
    while c != 2:
        print('Введите координаты (через пробел)')
        str = input()
        x = int(str[-1])
        y = int(str[0])
        if arr[x-1][y-1] == 1:
            arr[x-1][y-1] = '+'
            c+=1
            print('Попадение!')
        else:
            arr[x - 1][y - 1] = '-'
            print('Промах!')
        for i in arr:
            print(i)
    print('ПОБЕДА!!!')
    return 0
def random_ships(arr):
    while 1:
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        for i in range(2):
            x1 = random.randint(0, 4)
            y1 = random.randint(0, 4)
            x2 = random.randint(0, 4)
            y2 = random.randint(0, 4)
            if [x1, y1] != [x2, y2]:
                if [x2, y2] != [x1, y1 + 1] and [x2, y2] != [x1, y1 - 1] and [x2, y2] != [x1 + 1, y1] and [x2, y2] != [x1 - 1, y1]:
                    arr[x1][y1] = 1
                    arr[x2][y2] = 1
                    return arr


new = random_ships(array)
for i in new:
    print(i)

game(new)