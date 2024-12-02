from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_markup():
    # Создаём объекты кнопок.
    button_1 = InlineKeyboardButton(text="Собаки 🦮", callback_data="dog")
    button_2 = InlineKeyboardButton(text="Кошки 🐈", callback_data="cat")


    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1, button_2)
    return keyboard