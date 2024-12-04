from handlers.custom_handlers.command_history import add_history
from loader import bot
from states.translate import Translater
from telebot.types import Message
from api.Translater import get_langs, lookup
from keyboards.reply.translate import gen_markup
from telebot.types import ReplyKeyboardRemove



@bot.message_handler(commands=['translate_start'])
def start_translate(message: Message) -> None:
    bot.set_state(message.from_user.id, Translater.base, message.chat.id)
    global langs_response
    langs_response = get_langs()
    if langs_response.status_code != 200:
        bot.send_message(message.from_user.id,'Ой, похоже переводчик не доступен, приносим свои извинения')
    else:
        bot.send_message(message.from_user.id,
                         f"Переводчик готов к работе ")
        bot.send_message(message.from_user.id, "Выбери язык с помощью команды set_lang")
    add_history(message)


@bot.message_handler(commands=['set_lang'])
def give_lang(message: Message) -> None:
    bot.set_state(message.from_user.id, Translater.lang, message.chat.id)
    global langs
    langs = langs_response.json()
    bot.send_message(message.from_user.id, 'Выберите одно из доступных направлений перевода')
    bot.send_message(message.from_user.id, ", ".join(map(str, langs)))
    bot.send_message(message.from_user.id, "Самые популярные направления перевода:", reply_markup=gen_markup())
    add_history(message)


@bot.message_handler(func=lambda message: message.text == "ru-en")
@bot.message_handler(func=lambda message: message.text == "en-ru")
@bot.message_handler(state=Translater.lang)
def sets_lang(message: Message) -> None:
    if message.text in langs:
        global lang
        lang = message.text
        bot.send_message(message.from_user.id, f"Выбраны языки {lang}",reply_markup=ReplyKeyboardRemove())
        bot.set_state(message.from_user.id, "*")
    else:
        bot.send_message(message.from_user.id, 'Такого направления нет. Попробуйте ещё раз')

@bot.message_handler(commands=['translate'])
def translate(message: Message) -> None:
    bot.set_state(message.from_user.id, Translater.lookup, message.chat.id)
    bot.send_message(message.from_user.id, "Введите одно слово для перевода")
    add_history(message)


@bot.message_handler(state=Translater.lookup)
def set_slovo(message: Message) -> None:
    text = message.text
    lookup_response = lookup(lang, text)
    if lookup_response.status_code != 200:
        bot.send_message(message.from_user.id, 'Не удалось выполнить перевод:', lookup_response.text)
    result = lookup_response.json()
    try:
        bot.send_message(message.from_user.id, f"Слово {text} переводится как {result["def"][0]["tr"][0]["text"]}\n"
                                               f"Для ввода нового слова введите команду /translate")
        bot.set_state(message.from_user.id, "*")
    except IndexError:
        bot.send_message(message.from_user.id, 'Не удалось выполнить перевод')
        bot.set_state(message.from_user.id, "*")