## Задача 2. В первом списке находится информация об ассортименте мороженного, 
## во втором списке - информация о том, какое мороженное есть на складе. 
## Выведите названия того товара, который закончился.
## Пример:
## 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
## 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
## Ответ. Закончилось: «Бурёнка»

list_1 = {
        'Сливочное', 
        'Бурёнка', 
        'Вафелька', 
        'Сладкоежка'
}
list_2 = {
        'Сливочное', 
        'Вафелька', 
        'Сладкоежка'
}

list_difference = []
for element in list_1:
    if element not in list_2:
        list_difference.append(element)

print(list_difference)