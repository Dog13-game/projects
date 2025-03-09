


import telebot
from telebot import types

# Токен бота
TOKEN = "7421404546:AAHklHP0Ai5VaG9aMRkgPZt7nndIJWhdlH8"
bot = telebot.TeleBot(TOKEN)

# Словник конвертації одиниць вимірювання
CONVERSIONS = {
    'об\'єм': {'чашка': 240, 'столова ложка': 15, 'чайна ложка': 5, 'склянка': 250},
    'вага': {'кілограм': 1000, 'грам': 1, 'фунт': 453.592, 'унція': 28.3495}
}

# Функція конвертації
def convert_units(value, unit, category):
    if category in CONVERSIONS and unit in CONVERSIONS[category]:
        return value * CONVERSIONS[category][unit]
    return None

# Стартова команда
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(types.KeyboardButton("Об'єм"), types.KeyboardButton("Вага"))
    bot.send_message(
        message.chat.id,
        "🍽️ Привіт! Я ваш кулінарний бот 🧑‍🍳.\n"
        "Обери категорію або введи значення у форматі:\n"
        "`<кількість> <одиниця вимірювання>`\n"
        "Наприклад: `2 чашка`\n\n"
        "Доступні категорії:\n- Об'єм: чашка, столова ложка, чайна ложка, склянка\n- Вага: кілограм, грам, фунт, унція",
        parse_mode="Markdown",
        reply_markup=markup
    )

# Обробка вибору категорії
@bot.message_handler(func=lambda message: message.text in ["Об'єм", "Вага"])
def handle_category(message):
    category = message.text.lower()
    units = ", ".join(CONVERSIONS[category].keys())
    bot.send_message(
        message.chat.id,
        f"Ви обрали категорію: {category}\n"
        f"Доступні одиниці: {units}\n"
        "Введіть значення у форматі: `<кількість> <одиниця вимірювання>`\nНаприклад: `2 чашка`",
        parse_mode="Markdown"
    )

# Обробка текстових повідомлень для конвертації
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        parts = message.text.lower().split()
        value = float(parts[0])
        unit = ' '.join(parts[1:])

        # Визначаємо категорію одиниці вимірювання
        category = next((cat for cat, units in CONVERSIONS.items() if unit in units), None)

        if category:
            result = convert_units(value, unit, category)
            bot.send_message(message.chat.id, f"✅ {value} {unit} дорівнює {result:.2f} мл/г.")
        else:
            bot.send_message(message.chat.id, "⚠️ Невідома одиниця вимірювання. Спробуйте ще раз.")
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, "⚠️ Помилка! Введіть у форматі: `<кількість> <одиниця вимірювання>`.")

# Запуск бота
bot.polling()
