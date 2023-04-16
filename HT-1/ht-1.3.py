## Задача 3. Напишите программу, которая по заданному номеру четверти, 
## показывает диапазон возможных координат точек в этой четверти (x и y).
## 1 -> x > 0, y > 0

numSq = input('Введите номер четверти: ')
numSq = int(numSq)
if 4 >= numSq >= 1:
    if numSq == 1:
        print('x > 0, y > 0')
    elif numSq == 2:
        print('x > 0, y < 0')
    elif numSq == 3:
        print('x < 0, y < 0')
    elif numSq == 4:
        print('x < 0, y > 0')
else:
    print('Номер четверти от 1 до 4')