## Задача 1. Создайте пользовательский аналог метода map().

def my_map(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result