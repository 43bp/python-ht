## Задача 3. Создайте скрипт бота, который находит ответы на фразы 
## по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», 
## «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

data = open('dictionary.txt', encoding = 'utf-8')
text = data.readlines()
data.close()

phrase = text[0].split(':')


bot = {}
bot[phrase[0]] = phrase[1]
phrase = input('Поговорите с Игорем: ')
print(bot[input])