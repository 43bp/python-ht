## Задача 2. Дан список случайных чисел. 
## Создайте список, в который попадают числа, 
## описывающие случайную возрастающую последовательность. 
## Порядок элементов менять нельзя.
## [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)

def get_up(numbers):
    ups = [numbers[0]]
    for i in numbers:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up(numbers))