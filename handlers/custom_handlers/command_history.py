from loader import bot
from telebot.types import Message
from database.models import Commands
import datetime
from typing import List


@bot.message_handler(commands=["history"])
def get_history(message: Message):
    command: List[Commands] = Commands.select().order_by(-Commands.command_id).limit(10)

    result = []
    result.extend(map(str, reversed(command)))

    bot.send_message(message.from_user.id, "\n".join(result))
    add_history(message)


def add_history(message: Message) -> None:
    user_id = message.from_user.id
    due_date = datetime.datetime.now()
    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"] = {"user_id": user_id}
        data["new_task"]["title"] = message.text
        data["new_task"]["due_date"] = due_date
        new_task = Commands(**data["new_task"])
        new_task.save()
