

import telebot
from config import token  # из файла config.py забираем нашу переменную с токеном


# Создаем экземпляр бота
bot = telebot.TeleBot('6127790797:AAEryyGpirx7UysGFc-moT3yGgsbPLe_eMw')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши мне что-нибудь )')

import random
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()




