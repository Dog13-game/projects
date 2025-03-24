


import telebot
import random

# Токен бота
TOKEN = '7421404546:AAHklHP0Ai5VaG9aMRkgPZt7nndIJWhdlH8'
bot = telebot.TeleBot(TOKEN)

# ID користувача
CHAT_ID = 5249607313

# Обробка команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привіт! У мене є такі функції:\n- Надсилання мемів (команда: /meme)\n- Конвертація величин (команда: /converts)\n- Жарти (команда: /joke)"
    )

# Функція для конвертації величин
def convert_units(value, from_unit, to_unit):
    # Словник коефіцієнтів для конвертації
    conversions = {
        'метри': {'фути': 3.28084, 'сантиметри': 100, 'міліметри': 1000},
        'фути': {'метри': 0.3048, 'сантиметри': 30.48, 'міліметри': 304.8},
        'сантиметри': {'метри': 0.01, 'фути': 0.0328084, 'міліметри': 10},
        'міліметри': {'метри': 0.001, 'фути': 0.00328084, 'сантиметри': 0.1},
    }
    if from_unit in conversions and to_unit in conversions[from_unit]:
        # Виконати конвертацію
        return value * conversions[from_unit][to_unit]
    else:
        return None

# Обробка команди /converts
@bot.message_handler(commands=['converts'])
def converts_command(message):
    bot.send_message(
        message.chat.id,
        "Введіть запит для конвертації у форматі: <значення> <одиниця> в <цільова одиниця>.\n"
        "Наприклад: 15 метри в фути"
    )

    @bot.message_handler(func=lambda message: True)
    def handle_converts(message):
        text = message.text.lower()
        try:
            # Розділяємо текст на частини
            parts = text.split(" в ")
            if len(parts) != 2:
                raise ValueError("Неправильний формат запиту.")
            value_and_from_unit = parts[0].split()
            to_unit = parts[1]

            # Визначаємо кількість значень і одиниці вимірювання
            if len(value_and_from_unit) != 2:
                raise ValueError("Неправильний формат запиту.")

            value = float(value_and_from_unit[0])
            from_unit = value_and_from_unit[1]

            # Конвертуємо величину
            result = convert_units(value, from_unit, to_unit)

            if result is not None:
                bot.send_message(
                    message.chat.id,
                    f"{value} {from_unit} = {result:.2f} {to_unit}"
                )
            else:
                bot.send_message(message.chat.id, " Перепрошую, я не можу виконати цю конвертацію.")
        except ValueError:
            bot.send_message(
                message.chat.id,
                "Неправильний формат запиту. Введіть у форматі: <значення> <одиниця> в <цільова одиниця>.\n"
                "Наприклад: 15 метри в фути."
            )

# Шлях до папки, де зберігаються меми
UPLOAD_FOLDER = "C:/Users/XXX/Desktop/memes/"

# Список, де ми зберігатимемо назви файлів з мемами
memes = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

# Обробка отримання фото
@bot.message_handler(content_types=['photo'])
def receive_meme(message):
    # Дістаємо інформацію про надісланий файл з мемом
    file_info = bot.get_file(message.photo[-1].file_id)
    # Завантажуємо файл з мемом
    downloaded_file = bot.download_file(file_info.file_path)
    # Зберігаємо мем на комп'ютері під унікальним іменем
    file_name = f"{len(memes) + 1}.jpg"
    with open(f"{UPLOAD_FOLDER}{file_name}", 'wb') as new_file:
        new_file.write(downloaded_file)
    # Додаємо назву мема в список memes
    memes.append(file_name)
    bot.reply_to(message, "Мем отримано і збережено!")

# Обробка команди /meme
@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        # Вибираємо випадковий мем
        meme = random.choice(memes)
        meme_path = f"{UPLOAD_FOLDER}{meme}"

        # Перевіряємо, чи існує файл
        import os
        if os.path.exists(meme_path):
            # Надсилаємо мем
            with open(meme_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        else:
            bot.reply_to(message, f"⚠️ Мем {meme} відсутній у папці.")
    else:
        bot.reply_to(message, "⚠️ Мемів поки немає :(")



# Список жартів
jokes = [
    "Ваші документи?\n– Мої документи.\n– Пред’явіть документи!\n– А нащо вам?\n– Хочу подивитись.\n– Купіть собі і дивіться.\n– Ви що хворий?\n– А ви що лікар?\n– Я інспектор ДАІ.\n– А я електрик.\n– Ви що пили?\n– Пив і їв, а що не можна було?\n– Ви що клоун?\n– А ви хочете в цирк?\n– Хочу ваші документи перевірити!\n– А я хочу на море.\n– У вас всі вдома?\n– А ви хочете в гості?..\n– Я вам зараз штраф випишу!\n– А газету теж можете виписати?\n– Та ви псих! Їдьте звідси щоб я вас не бачив!",
    "Випадок в маршрутці:\n– Чоловіче, заберіть свою собаку, а то мені блохи скачуть!\n– Тузік, відійди, не бачиш – в жінки блохи.",
    "Учора вперше ходив на полювання. Після 12-го чи 13-го пострілу качка померла від сміху.",
    "Що робить код, коли сумує? Дебаг!",
    "Шановні виробники телевізорів, зробіть таку кнопочку на телевізорі, на яку натискаєш – і пульт пищить, де він там валяється.",
    "Вчителька біології доводить учням шкоду алкоголю. Бере черв’яка, кидає в стакан зі спиртом\n– Той здох.\nКидає черв’яка в склянку з водою – той живе.\n– Діти, який висновок з цього можна зробити?\nВовочка:\n– Якщо пити спирт, то глистів не буде!"
]

# Обробка команди /joke
@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(jokes)  # Вибираємо випадковий жарт
    bot.send_message(message.chat.id, joke)





# Запуск бота
bot.polling()
