from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from handlers.custom_handlers.command_history import add_history
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
    add_history(message)

