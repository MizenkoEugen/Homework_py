# Игра с конфетами

import telebot
import random

bot = telebot.TeleBot("5932424939:AAGQ5qNY5F2XvRXrFCYotb6WaCg7Y3BErJo")

flag = None
sweets = 221
max_sweet = 28


@bot.message_handler(commands=["restart"])
def start(message):
    global sweets, flag
    sweets = 221
    bot.send_message(message.chat.id, f"Приветствую вас в игре!")
    flag = random.choice(["user", "bot"])
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    if flag == "user":
        bot.send_message(message.chat.id, f"Первым ходите вы")
    else:
        bot.send_message(message.chat.id, f"Первым ходит бот")
    controller(message)


@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Приветствую вас в игре!")
    flag = random.choice(["user", "bot"])
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    if flag == "user":
        bot.send_message(message.chat.id, f"Первым ходите вы")
    else:
        bot.send_message(message.chat.id, f"Первым ходит бот")
    controller(message)


def controller(message):
    global flag
    if sweets > 0:
        if flag == "user":
            bot.send_message(
                message.chat.id, f"Ваш ход введите кол-во конфет от 0 до {max_sweet}")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(
            message.chat.id, f"Победил {flag}, для перезапуска введите /restart")


def bot_input(message):
    global sweets, flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % (max_sweet + 1)
    if bot_turn == 0:
        bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)


def user_input(message):
    global sweets, flag
    user_turn = int(message.text)
    if 0 < user_turn <= max_sweet:
        sweets -= user_turn
        bot.send_message(message.chat.id, f"осталось {sweets}")
        flag = "user" if flag == "bot" else "bot"
    else:
        bot.send_message(message.chat.id, f"Введено недопустимое число")
    controller(message)


bot.infinity_polling()
