## Задача 1. Дано натуральное число N. 
## Найдите значение выражения: N + NN + NNN
## N может быть любой длины.
## N = 132: 132 + 132132 + 132132132 = 132264396

n = int(input("Введите число n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)