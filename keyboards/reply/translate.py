from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def gen_markup():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="ru-en")
    button_2 = KeyboardButton(text="en-ru")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1, button_2)
    return keyboard