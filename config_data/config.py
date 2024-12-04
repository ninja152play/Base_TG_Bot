import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

DATE_FORMAT = "%d.%m.%Y"
DB_PATH = "database.db"
BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("history", "История запросов"),
    ("survey", "Опрос"),
    ("answer", "Кот или собака"),
    ("translate_start", "Запуск переводчик"),
    ("set_lang", "Выбор языка" ),
    ("translate", "Ввод слова" ),
    ("start_task", "Запустить менеджер задач"),
    ("newtask", "Создать задачу"),
    ("tasks", "Последние 10 задач"),
    ("today", "Задачи на сегодня"),
)

