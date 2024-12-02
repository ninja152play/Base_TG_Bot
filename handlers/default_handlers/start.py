from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}! Я являюсь тестовым ботом и имею ряд функций")
    bot.reply_to(message, f"{message.from_user.full_name}! Напиши команду /help для того чтобы увидеть все что я умею")
