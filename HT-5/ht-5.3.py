## Задача 3. Задайте список случайных чисел от 1 до 10. 
## Посчитайте, сколько всего совпадающих элементов есть в списке. 
## Удалите все повторяющиеся элементы.
## [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
## [1, 4, 2, 3, 6, 7]

import random

numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)

temp = [] 
for x in numbers: 
    if x not in temp:
        temp.append(x)
ints_list = temp

s = set(numbers)
for i in s:
    print(f"'{i}': {numbers.count(i)}")

print(f'Список уникальных элементов {temp}')