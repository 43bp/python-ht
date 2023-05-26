## Добавьте в telegram-бота игру «Угадай числа». 
## Бот загадывает число от 1 до 1000. 
## Когда игрок угадывает его, бот выводит количество сделанных ходов.

import random
import telebot
from telebot import types
import logging

bot = telebot.TeleBot('6081591511:AAEu2ohEmI7tQqcMQlxRZXLvEPYNAWBKFQc')
telebot.logger.setLevel(logging.INFO)

storage = dict()

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def command_text_hi(m):
    bot.send_message(m.chat.id, "Ну привет)")

@bot.message_handler(func=lambda message: message.text.lower() == "как дела")
def command_text_dela(m):
    bot.send_message(m.chat.id, "хорошо")

@bot.message_handler(func=lambda message: message.text.lower() == "игра")
def digitgames(message):
    init_storage(message.chat.id) ### Инициализирую хранилище

    attempt = 999
    set_data_storage(message.chat.id, "attempt", attempt)

    bot.send_message(message.chat.id, f'Игра "угадай число"!\nКоличество попыток: {attempt}')

    random_digit=random.randint(1, 1000)
    print(random_digit)

    set_data_storage(message.chat.id, "random_digit", random_digit)
    print(get_data_storage(message.chat.id))
 
    bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 1000!')
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message, process_digit_step)

def process_digit_step(message):
    user_digit = message.text
    
    if not user_digit.isdigit():
            msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
            bot.register_next_step_handler(msg, process_digit_step)
            return

    attempt = get_data_storage(message.chat.id)["attempt"]
    random_digit = get_data_storage(message.chat.id)["random_digit"]

    if int(user_digit) == random_digit:
        bot.send_message(message.chat.id, f'Ура! Ты угадал число! Это была цифра: {random_digit}')
        init_storage(message.chat.id) ### Очищает значения из хранилище
        return
    elif attempt > 1:
        attempt-=1
        set_data_storage(message.chat.id, "attempt", attempt)
        bot.send_message(message.chat.id, f'Неверно, осталось попыток: {attempt}')
        bot.register_next_step_handler(message, process_digit_step)
    else:
        bot.send_message(message.chat.id, 'Вы проиграли!')
        init_storage(message.chat.id) ### Очищает значения из хранилище
        return
            


if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling()
