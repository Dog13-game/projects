
import tkinter as tk
import time

# Секундомір
def start_stopwatch():
    start_time = time.time()
    label_stopwatch.config(text="Секундомір запущено! Натисніть 'Зупинити', щоб зупинити.")
    btn_stopwatch_start.config(state=tk.DISABLED)
    btn_stopwatch_stop.config(state=tk.NORMAL)

    def stop_stopwatch():
        elapsed_time = time.time() - start_time
        label_stopwatch.config(text=f"Час: {elapsed_time:.2f} секунд")
        btn_stopwatch_start.config(state=tk.NORMAL)
        btn_stopwatch_stop.config(state=tk.DISABLED)

    btn_stopwatch_stop.config(command=stop_stopwatch)

# Конвертер валют
def currency_converter():
    try:
        cash = float(entry_cash.get())
    except ValueError:
        label_converter_result.config(text="Ви ввели неправильне значення або порожній рядок")
    else:
        convert = entry_currency.get().upper()
        if convert == "EUR":
            result = cash / 43
        elif convert == "USD":
            result = cash / 42
        elif convert == "ZL":
            result = cash / 10
        elif convert == "JPY":
            result = cash / 0.27
        else:
            result = None
        if result is not None:
            label_converter_result.config(text=f"{cash} гривень це {result:.2f} {convert}")
        else:
            label_converter_result.config(text="Некоректна валюта")
    finally:
        entry_cash.delete(0, tk.END)
        entry_currency.delete(0, tk.END)

# Функції телефонної книги
contacts = {}

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    contacts[name] = phone
    label_phonebook_result.config(text=f"Контакт {name} додано.")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        label_phonebook_result.config(text=f"Контакт {name} видалено.")
    else:
        label_phonebook_result.config(text=f"Контакт {name} не знайдено.")
    entry_name.delete(0, tk.END)

def search_contact():
    name = entry_name.get()
    if name in contacts:
        label_phonebook_result.config(text=f"{name}: {contacts[name]}")
    else:
        label_phonebook_result.config(text=f"Контакт {name} не знайдено.")
    entry_name.delete(0, tk.END)

def list_contacts():
    if contacts:
        contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        label_phonebook_result.config(text=contact_list)
    else:
        label_phonebook_result.config(text="Телефонна книга порожня.")

# Головне меню
def show_main_menu():
    frame_stopwatch.pack_forget()
    frame_converter.pack_forget()
    frame_phonebook.pack_forget()
    frame_calculator.pack_forget()
    frame_main.pack()

# Показ секундоміра
def show_stopwatch():
    frame_main.pack_forget()
    frame_converter.pack_forget()
    frame_phonebook.pack_forget()
    frame_calculator.pack_forget()
    frame_stopwatch.pack()

# Показ конвертера валют
def show_converter():
    frame_main.pack_forget()
    frame_stopwatch.pack_forget()
    frame_phonebook.pack_forget()
    frame_calculator.pack_forget()
    frame_converter.pack()

# Показ телефонної книги
def show_phonebook():
    frame_main.pack_forget()
    frame_stopwatch.pack_forget()
    frame_converter.pack_forget()
    frame_calculator.pack_forget()
    frame_phonebook.pack()

# Показ калькулятора
def show_calculator():
    frame_main.pack_forget()
    frame_stopwatch.pack_forget()
    frame_converter.pack_forget()
    frame_phonebook.pack_forget()
    frame_calculator.pack()

# Головне вікно
root = tk.Tk()
root.title("Програма з декількома функціями")
root.geometry("600x600")  # Встановлення розмірів головного вікна

# Головне меню
frame_main = tk.Frame(root)
frame_main.pack(pady=10)

btn_stopwatch_menu = tk.Button(frame_main, text="Секундомір", command=show_stopwatch)
btn_stopwatch_menu.pack(pady=5)

btn_converter_menu = tk.Button(frame_main, text="Конвертер валют", command=show_converter)
btn_converter_menu.pack(pady=5)

btn_phonebook_menu = tk.Button(frame_main, text="Телефонна книга", command=show_phonebook)
btn_phonebook_menu.pack(pady=5)

btn_calculator_menu = tk.Button(frame_main, text="Калькулятор", command=show_calculator)
btn_calculator_menu.pack(pady=5)

# Секундомір
frame_stopwatch = tk.Frame(root)

btn_stopwatch_start = tk.Button(frame_stopwatch, text="Запустити секундомір", command=start_stopwatch)
btn_stopwatch_start.pack()

btn_stopwatch_stop = tk.Button(frame_stopwatch, text="Зупинити секундомір", state=tk.DISABLED)
btn_stopwatch_stop.pack()

label_stopwatch = tk.Label(frame_stopwatch, text="")
label_stopwatch.pack(pady=10)

btn_back_from_stopwatch = tk.Button(frame_stopwatch, text="Назад в меню", command=show_main_menu)
btn_back_from_stopwatch.pack()

# Конвертер валют
frame_converter = tk.Frame(root)

label_cash = tk.Label(frame_converter, text="Сума:")
label_cash.pack()
entry_cash = tk.Entry(frame_converter)
entry_cash.pack()

label_currency = tk.Label(frame_converter, text="Валюта (EUR/USD/zl/JPY):")
label_currency.pack()
entry_currency = tk.Entry(frame_converter)
entry_currency.pack()

btn_converter = tk.Button(frame_converter, text="Конвертувати", command=currency_converter)
btn_converter.pack()

label_converter_result = tk.Label(frame_converter, text="")
label_converter_result.pack(pady=10)

btn_back_from_converter = tk.Button(frame_converter, text="Назад в меню", command=show_main_menu)
btn_back_from_converter.pack()

# Телефонна книга
frame_phonebook = tk.Frame(root)

label_name = tk.Label(frame_phonebook, text="Ім'я:")
label_name.pack()
entry_name = tk.Entry(frame_phonebook)
entry_name.pack()
label_phone = tk.Label(frame_phonebook, text="Телефон:")
label_phone.pack()
entry_phone = tk.Entry(frame_phonebook)
entry_phone.pack()

btn_add = tk.Button(frame_phonebook, text="Додати контакт", command=add_contact)
btn_add.pack()

btn_delete = tk.Button(frame_phonebook, text="Видалити контакт", command=delete_contact)
btn_delete.pack()

btn_search = tk.Button(frame_phonebook, text="Пошук контакту", command=search_contact)
btn_search.pack()

btn_list = tk.Button(frame_phonebook, text="Вивести всі контакти", command=list_contacts)
btn_list.pack()

label_phonebook_result = tk.Label(frame_phonebook, text="")
label_phonebook_result.pack(pady=10)

btn_back_from_phonebook = tk.Button(frame_phonebook, text="Назад в меню", command=show_main_menu)
btn_back_from_phonebook.pack()

# Калькулятор
frame_calculator = tk.Frame(root)

current_expression = ""

def on_button_click(button):
    global current_expression
    if button == "C":
        current_expression = ""
        display.delete(0, tk.END)
    elif button == "=":
        try:
            result = eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Помилка")
            current_expression = ""
    else:
        current_expression += str(button)
        display.delete(0, tk.END)
        display.insert(0, current_expression)

def set_theme(theme):
    if theme == "light":
        root.config(bg='white')
        display.config(bg='lightgray', fg='black')
    elif theme == "dark":
        root.config(bg='black')
        display.config(bg='gray', fg='white')
    elif theme == "yellow":
        root.config(bg='#faee02')
        display.config(bg='#facd05', fg='black')
    elif theme == "blue":
        root.config(bg='#05faea')
        display.config(bg='#facd05', fg='black')

    for button in buttons:
        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'lightblue', fg='black' if theme != "dark" else 'white')

display = tk.Entry(frame_calculator, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = []
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+', '.', '**'
]

row_val = 1
col_val = 0

# Створюємо кнопки:
for text in button_texts:
    button = tk.Button(frame_calculator, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# МЕНЮ для калькулятора
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
theme_menu.add_command(label="Жовта тема", command=lambda: set_theme("yellow"))
theme_menu.add_command(label="Блакитна тема", command=lambda: set_theme("blue"))
menubar.add_cascade(label="Налаштування", menu=theme_menu)

root.config(menu=menubar)

btn_back_from_calculator = tk.Button(frame_calculator, text="Назад в меню", command=show_main_menu)
btn_back_from_calculator.grid(row=row_val+1, column=0, columnspan=4)

def set_theme(theme):

    if theme == "light":

        root.config(bg='white')

        display.config(bg='lightgray', fg='black')

    elif theme == "dark":

        root.config(bg='black')

        display.config(bg='gray', fg='white')

    elif theme == "yelow":

        root.config(bg='#faee02')

        display.config(bg='#facd05', fg='black')

    elif theme == "blue":

        root.config(bg='#05faea')

        display.config(bg='#facd05', fg='black')

    for button in buttons:

        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'lightblue', fg='black' if theme != "dark" else 'white')



# МЕНЮ
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
theme_menu.add_command(label="Жовта тема", command=lambda: set_theme("yelow"))
theme_menu.add_command(label="Блакитна тема", command=lambda: set_theme("blue"))
menubar.add_cascade(label="Налаштування", menu=theme_menu)

root.mainloop()
