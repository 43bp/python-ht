## Задача 1. Напишите программу, которая принимает на вход число N 
## и выдает список факториалов для чисел от 1 до N.
## пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите натуральное число: '))
nums = []
value = 1
for i in range(1, n + 1):
    nums.append(value)
    value *= i + 1
print(nums)