## Задача 2. В списке находятся названия фруктов. 
## Выведите все фрукты, названия которых начинаются на заданную букву.
## а –> абрикос, авокадо, апельсин, айва.

list = ['апельсин', 'мандарин', 'мараккуя', 'лимон', 'авокадо','лайм','малина','арбуз']
letter = str(input('Введите букву, на которую начинается фрукт: '))
print("Список всех фруктов " + str(list))
res = [idx for idx in list if idx[0].lower() == letter.lower()]
print("Фрукты, которые начинаются на букву " + letter + str(res))