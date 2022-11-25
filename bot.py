import telebot
import random
import schedule
import time
import deepl

from random import randint
from configs import Token


bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(message):
    def pseudorandom():
        splitlines = open('Дмитрий Йокубаускас.txt', encoding="utf8").read().splitlines()
        randomised = random.choice(splitlines)
        bot.send_message(message.chat.id, randomised)

    # def randomised():
    #     timeset = random.randint(1, 10)
    #     return timeset
    schedule.every(1).seconds.do(pseudorandom)

    while True:
        delay = randint(1, 1000)
        print("Sleep " + str(delay))
        schedule.run_pending()
        time.sleep(delay)


@bot.message_handler(commands=['help', 'stop'])
def start(message):
    bot.send_message(message.chat.id, 'Пошел нахуй')


@bot.message_handler()
def send_reply(message):
    if message.from_user.id == 584139440:
        def pseudorandom():
            splitlines = open('Оскорбления.txt', encoding="utf8").read().splitlines()
            randomised = random.choice(splitlines)
            time.sleep(5)
            return randomised

        bot.reply_to(message, pseudorandom())


if __name__ == '__main__':
    bot.polling(none_stop=True)
