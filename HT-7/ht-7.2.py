### Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def repeat(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator