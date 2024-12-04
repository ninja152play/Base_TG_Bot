from loader import bot
from telebot.types import Message
from keyboards.reply.catdog import gen_markup
from handlers.custom_handlers.command_history import add_history

@bot.message_handler(commands=["answer"])
def start_message(message: Message) -> None:
    bot.send_message(message.from_user.id, "Какое животное тебе нравится больше?", reply_markup=gen_markup())
    add_history(message)


@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "dog"
    )
)
def dog_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "Я тоже люблю собак, они так мило машут хвостиком!",
    )

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data  # Обращаемся к callback_data, указанной при создании кнопки.
        == "cat"
    )
)
def cat_answer(callback_query):
    # Удаляем клавиатуру.
    bot.edit_message_reply_markup(
        callback_query.from_user.id, callback_query.message.message_id
    )
    # Отправляем сообщение пользователю.
    bot.send_message(
        callback_query.from_user.id,
        "Я тоже люблю кошек, они так умилительно мурлыкают!",
    )