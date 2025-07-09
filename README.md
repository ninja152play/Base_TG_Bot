# Многофункциональный Telegram-бот

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Telegram](https://img.shields.io/badge/Telegram_Bot_API-✓-blue)
![SQLite](https://img.shields.io/badge/SQLite-✓-green)

## 📌 Описание проекта

Универсальный Telegram-бот с функциями:
- 🗂 Менеджер задач
- 🌍 Многоязычный переводчик
- 📝 Опросы и анкетирование
- 📊 История запросов

**Цель проекта**: Освоение современных технологий:
- Работа с API (Yandex Dictionary)
- Базы данных (SQLite3 + Peewee ORM)
- Виртуальные окружения (venv)
- Асинхронное программирование

## 🚀 Основные команды

### 🔄 Переводчик
| Команда | Описание |
|---------|----------|
| `/translate_start` | Запуск переводчика + список языков |
| `/set_lang` | Выбор языка перевода |
| `/translate` | Перевод введенного слова |

### ✅ Менеджер задач
| Команда | Описание |
|---------|----------|
| `/start_task` | Запуск менеджера задач |
| `/newtask` | Создание новой задачи |
| `/tasks` | Последние 10 задач |
| `/today` | Задачи на сегодня |

### 📊 Дополнительные функции
| Команда | Описание |
|---------|----------|
| `/history` | История ваших запросов |
| `/survey` | Анкета (имя, возраст и др.) |
| `/answer` | Голосование "Коты vs Собаки" |

## 🌐 Используемые API
```python
# Получение списка языков
GET https://dictionary.yandex.net/api/v1/dicservice.json/getLangs

# Перевод слова
POST https://dictionary.yandex.net/api/v1/dicservice.json/lookup
```
## 💻 Установка и запуск
### Первый запуск
```bash
git clone https://github.com/ninja152play/Base_TG_Bot.git
cd Base_TG_Bot
python -m venv venv

# Для Windows:
.\venv\Scripts\activate.bat

# Для Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

# Заполните .env по примеру .env.example
python main.py
```
### Повторный запуск
```bash
cd Base_TG_Bot
.\venv\Scripts\activate.bat  # Активируем окружение
python main.py
```
## 🛠 Режим разработки
Откройте проект в PyCharm/VSCode

Активируйте виртуальное окружение:

```bash
.\venv\Scripts\activate
Запустите main.py
```

## 📊 Примеры работы
Перевод слова
```json
{
  "text": "торт",
  "translation": "cake",
  "language_pair": "ru-en"
}
```
Создание задачи
```text
✅ Новая задача: "Купить молоко" (на сегодня)
```
## 👨‍💻 Разработчик
@ninja152play (Илья Тарасов)

## Note:
Для получения токена бота обратитесь к BotFather в Telegram
