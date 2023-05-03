## Задача 1. Дано натуральное число N. 
## Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
## 60 -> 2, 2, 3, 5

def primeNum(numN):
    primeList = []
    for i in range(2, numN):
        while numN % i == 0:
            numN /= i
            primeList.append(i)
    return primeList
numN = int(input("Введите натуральное число: "))
list = primeNum(numN)
print(f'Простые множители числа {numN}: {list}')