## Задача 4. Напишите программу, которая на вход принимает число (N), 
## а на выходе показывает все чётные числа от 1 до N.
## 5 -> 2, 4
## 8 -> 2, 4, 6, 8

n = input('Введите натуральное число: ')
n = int(n)

if n < 2:
    print ("Четных натуральных чисел в ряде нет")
else:
    i = 2;
    while i <= n:
        print (i, end=" ")
        i += 2