from telebot.handler_backends import State, StatesGroup


class Translater(StatesGroup):
    base = State()
    lang = State()
    lookup = State()
