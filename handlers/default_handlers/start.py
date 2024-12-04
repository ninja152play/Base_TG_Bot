from peewee import IntegrityError
from telebot.types import Message
from database.models import User
from loader import bot
from handlers.custom_handlers.command_history import add_history


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(message, f"Привет, {message.from_user.full_name}! Я являюсь тестовым ботом и имею ряд функций")
        bot.reply_to(message,
                     f"{message.from_user.full_name}! Напиши команду /help для того чтобы увидеть все что я умею")
    except IntegrityError:
        bot.reply_to(message, f"Рад вас снова видеть, {first_name}!")
    add_history(message)