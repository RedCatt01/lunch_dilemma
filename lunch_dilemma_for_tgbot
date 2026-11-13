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
    'Микки🐭 и обезьяны🙈', 
    'Чуфаня🥡'
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

me = bot.get_me()
print(f"--- ДИАГНОСТИКА ---")
print(f"Бот подключен: @{me.username} (ID: {me.id})")
print(f"Попытка отправки на CHAT_ID: {CHAT_ID}")

try:
    # 2. Проверяем, что это за чат с точки зрения Telegram
    chat_info = bot.get_chat(CHAT_ID)
    print(f"Telegram подтвердил чат! Название: '{chat_info.title}', Тип: {chat_info.type}")
except Exception as e:
    print(f"ОШИБКА TELEGRAM: {e}")

# 1. Выбираем случайный ресторан и отправляем в чат
bot.send_messages(
  chosen_rest= random.choice(RESTS)
  bot.send_message(CHAT_ID, f"Сегодня хороший день для обеда. Я уже выбрал место:\n{chosen_rest}")
)
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
