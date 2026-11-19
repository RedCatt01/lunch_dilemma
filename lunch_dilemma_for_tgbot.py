import os
import random
import telebot
from telebot import apihelper

# --- НАСТРОЙКИ ---
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])  # ID чата (обязательно с минусом)

# Список ресторанов
RESTS = [
    'Кореана🐉', 
    'Ипполит🥸',
    'Хачапури и вино🍷', 
    'Паста и вино🍝', 
    'Бюро🍔🍔',  
    'Чуфаня🥡'
]

# Пул для сообщения
MESS = [
    'Сегодня хороший день для обеда. Я уже выбрал место:',
    'Какой чудесный день! Какой чудесный пень! Какой чудесный я и место для обеда!',
    'Работа работой, а обед по расписанию!',
    'Работа не волк, волк - это ходить на обед.',
    'Чтобы мощность голода не превышала паспортных значений, необходимо уменьшить потери каллорий.',
    'Объявляю сБОУр на обед!'
]

# Настройки опроса
POLL_QUESTION = "Обед в 14?"
POLL_OPTIONS_1 = ["Я", "Не я"]
POLL_OPTIONS_2 = ["Да!!", "Не да"]
POLL_OPTIONS_3 = ["Иду", "Не иду"]
POLL_OPTIONS_4 = ["Конечно", "Нет"]
POLL_OPTIONS_5 = ["Поехали!", "Неа"]
POLL_OPTIONS_6 = ["+", "-"]
POLL_OPTIONS_7 = ["Есс", "Не сегодня"]
POLL_POLL_OPTIONS = [
    POLL_OPTIONS_1, 
    POLL_OPTIONS_2, 
    POLL_OPTIONS_3, 
    POLL_OPTIONS_4, 
    POLL_OPTIONS_5, 
    POLL_OPTIONS_6, 
    POLL_OPTIONS_7
    ]
IS_ANONYMOUS = False  # False — видно, кто как проголосовал; True — анонимно
# -----------------

bot = telebot.TeleBot(TOKEN)

# 1. Выбираем случайный ресторан и отправляем в чат
chosen_rest= random.choice(RESTS)
chosen_mess= random.choice(MESS)
bot.send_message(CHAT_ID, f"{chosen_mess}\n{chosen_rest}")

# 2. Отправляем опрос
POLL_OPTIONS = random.choice(POLL_POLL_OPTIONS)
bot.send_poll(
  chat_id=CHAT_ID,
  question=POLL_QUESTION,
  options=POLL_OPTIONS,
  is_anonymous=IS_ANONYMOUS,
)
print(f"Бот запущен!")
print("Сообщение и опрос успешно отправлены!")
