#!/usr/bin/env python3
# ============================================================
#  🐱 FELIKSOS MOBILE v1.5
#  📱 Terminal Edition for UserLAnd
#  🖤 Created by Kernel
# ============================================================

import os
import sys
import time
import random
from datetime import datetime, timedelta

# ============================================================
#  🎨 ЦВЕТА
# ============================================================
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

# ============================================================
#  🐱 ASCII-КОТ
# ============================================================
CAT = r"""
      /\_/\
     ( o.o )
      > ^ <
"""

# ============================================================
#  🌌 КОСМИЧЕСКИЕ ОБОИ
# ============================================================
def show_wallpaper():
    os.system('clear')
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════════╗
║{PURPLE}                    🌌 КОСМОС FELIKSOS 🌌                    {CYAN}║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║{YELLOW}        *        .        ✦        .        *                {CYAN}║
║{WHITE}     .        *        .        🌟        .        *          {CYAN}║
║{PURPLE}         ✦        🌌        .        ✦        .               {CYAN}║
║                                                              ║
║{BLUE}              🪐  ПЛАНЕТЫ  🪐  ЗВЁЗДЫ  🪐  КОСМОС              {CYAN}║
║                                                              ║
║{YELLOW}        .        *        ✦        .        *                {CYAN}║
║{WHITE}     *        .        🌟        .        *        .          {CYAN}║
║{PURPLE}         .        ✦        .        🌌        ✦               {CYAN}║
║                                                              ║
║{CYAN}                  🐱 FELIKSOS MOBILE v1.5 🐱                  {CYAN}║
║                                                              ║
║{YELLOW}              Добро пожаловать, Kernel!                       {CYAN}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")

# ============================================================
#  📋 СПРАВКА
# ============================================================
def show_help():
    print(f"""{YELLOW}
📋 ДОСТУПНЫЕ КОМАНДЫ:

  ОСНОВНЫЕ:
  help      — этот список
  version   — версия FeliksOS
  meow      — Феликс мяукает
  cat       — ASCII-кот
  cats      — Феликс и Пушок
  felix     — информация о Феликсе
  clear     — очистить экран
  exit      — выход

  ИНСТРУМЕНТЫ:
  calc      — калькулятор
  random    — случайное число
  timer     — таймер
  date      — дата и время
  notes     — заметки
  system    — информация о системе

  ИГРЫ И РАЗВЛЕЧЕНИЯ:
  game      — игра "Угадай число"
  ceasar    — шифр Цезаря
  cosmos    — анимация космоса
  market    — магазин FeliksOS

  НОВОЕ:
  build     — комната сборки
  addcmd    — добавить команду
  lore      — лор FeliksOS
  theme     — смена темы
  wallpaper — смена обоев
{RESET}""")

# ============================================================
#  🧮 КАЛЬКУЛЯТОР
# ============================================================
def calculator():
    print(f"{YELLOW}🧮 Калькулятор FeliksOS{RESET}")
    print("Введи выражение (например: 2 + 2)")
    print("Или 'back' для возврата.")
    
    while True:
        expr = input(f"{CYAN}calc> {RESET}").strip()
        if expr.lower() == 'back':
            break
        try:
            result = eval(expr)
            print(f"{GREEN}Результат: {result}{RESET}")
        except:
            print(f"{RED}Ошибка! Попробуй снова.{RESET}")

# ============================================================
#  🎲 СЛУЧАЙНОЕ ЧИСЛО
# ============================================================
def random_number():
    print(f"{YELLOW}🎲 Случайное число{RESET}")
    try:
        min_num = int(input("Минимум: "))
        max_num = int(input("Максимум: "))
        result = random.randint(min_num, max_num)
        print(f"{GREEN}🎲 Выпало: {result}{RESET}")
    except:
        print(f"{RED}Ошибка! Введи числа.{RESET}")

# ============================================================
#  ⏰ ТАЙМЕР
# ============================================================
def timer():
    print(f"{YELLOW}⏰ Таймер{RESET}")
    try:
        seconds = int(input("Секунды: "))
        print(f"{CYAN}⏳ Отсчёт пошёл...{RESET}")
        for i in range(seconds, 0, -1):
            print(f"\r{CYAN}Осталось: {i} сек{RESET}", end="")
            time.sleep(1)
        print(f"\n{GREEN}⏰ Время вышло!{RESET}")
    except:
        print(f"{RED}Ошибка! Введи число.{RESET}")

# ============================================================
#  📅 ДАТА И ВРЕМЯ (МСК)
# ============================================================
def show_date():
    now = datetime.now() + timedelta(hours=3)  # МСК
    print(f"{GREEN}📅 Дата: {now.strftime('%d.%m.%Y')}{RESET}")
    print(f"{GREEN}🕐 Время: {now.strftime('%H:%M:%S')} (МСК){RESET}")

# ============================================================
#  📝 ЗАМЕТКИ
# ============================================================
def notes():
    print(f"{YELLOW}📝 Заметки{RESET}")
    print("1. Показать заметки")
    print("2. Добавить заметку")
    print("3. Назад")
    
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == '1':
        try:
            with open(os.path.expanduser("~/feliksos_notes.txt"), "r") as f:
                print(f"{GREEN}{f.read()}{RESET}")
        except:
            print(f"{RED}Заметок пока нет.{RESET}")
    elif choice == '2':
        note = input("Заметка: ")
        with open(os.path.expanduser("~/feliksos_notes.txt"), "a") as f:
            f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M')}] {note}\n")
        print(f"{GREEN}✅ Заметка добавлена!{RESET}")

# ============================================================
#  📊 ИНФОРМАЦИЯ О СИСТЕМЕ
# ============================================================
def system_info():
    print(f"{YELLOW}📊 Информация о системе{RESET}")
    print(f"{GREEN}📱 ОС: FeliksOS Mobile v1.5{RESET}")
    print(f"{GREEN}🐧 Платформа: Debian (UserLAnd){RESET}")
    print(f"{GREEN}🐍 Python: {sys.version.split()[0]}{RESET}")
    print(f"{GREEN}📂 Домашняя папка: {os.path.expanduser('~')}{RESET}")

# ============================================================
#  🐱 ИНФОРМАЦИЯ О ФЕЛИКСЕ
# ============================================================
def felix_info():
    print(f"{CYAN}{CAT}{RESET}")
    print(f"{YELLOW}🐱 Феликс{RESET}")
    print(f"{GREEN}Роль: Дух FeliksOS{RESET}")
    print(f"{GREEN}Характер: Спокойный, загадочный, независимый{RESET}")
    print(f"{GREEN}Любит: Спать, гулять, наблюдать за хаосом{RESET}")
    print(f"{GREEN}Статус: Легенда{RESET}")

# ============================================================
#  🐱 ФЕЛИКС И ПУШОК
# ============================================================
def cats_info():
    print(f"{CYAN}{CAT}{RESET}")
    print(f"{YELLOW}🐱 Феликс{RESET}")
    print(f"{GREEN}Главный кот. Символ FeliksOS. Загадочный.{RESET}")
    print(f"{YELLOW}🐈 Пушок{RESET}")
    print(f"{GREEN}Серый напарник. Хранитель уюта. Спит на кровати.{RESET}")
    print(f"{PURPLE}Вместе — команда. Вместе — FeliksOS.{RESET}")

# ============================================================
#  🎮 ИГРА: УГАДАЙ ЧИСЛО
# ============================================================
def guess_game():
    print(f"{YELLOW}🎮 Угадай число!{RESET}")
    print("Я загадал число от 1 до 100.")
    
    secret = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input(f"{CYAN}Твой вариант: {RESET}"))
            attempts += 1
            
            if guess < secret:
                print(f"{BLUE}Больше!{RESET}")
            elif guess > secret:
                print(f"{BLUE}Меньше!{RESET}")
            else:
                print(f"{GREEN}🎉 Угадал! С {attempts} попыток!{RESET}")
                break
        except:
            print(f"{RED}Введи число!{RESET}")

# ============================================================
#  🔐 ШИФР ЦЕЗАРЯ
# ============================================================
def ceasar_cipher():
    print(f"{YELLOW}🔐 Шифр Цезаря{RESET}")
    print("1. Зашифровать")
    print("2. Расшифровать")
    print("3. Назад")
    
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == '1':
        text = input("Текст: ")
        shift = int(input("Сдвиг: "))
        result = ''.join(chr((ord(c) + shift) % 256) for c in text)
        print(f"{GREEN}Зашифровано: {result}{RESET}")
    elif choice == '2':
        text = input("Текст: ")
        shift = int(input("Сдвиг: "))
        result = ''.join(chr((ord(c) - shift) % 256) for c in text)
        print(f"{GREEN}Расшифровано: {result}{RESET}")

# ============================================================
#  🌌 КОСМОС (АНИМАЦИЯ)
# ============================================================
def cosmos_animation():
    stars = ['*', '.', '✦', '🌟', '✨', '·']
    for i in range(30):
        os.system('clear')
        print(f"{CYAN}🌌 КОСМОС FELIKSOS 🌌{RESET}\n")
        for _ in range(15):
            line = ''.join(random.choice(stars) if random.random() > 0.7 else ' ' for _ in range(60))
            print(f"{random.choice([CYAN, BLUE, PURPLE, WHITE])}{line}{RESET}")
        time.sleep(0.3)

# ============================================================
#  🛒 МАГАЗИН
# ============================================================
def market():
    balance = 0
    
    print(f"{YELLOW}🛒 FELIKSOS MARKET{RESET}")
    print(f"💰 Баланс: {balance} BTC")
    print("\n1. ⛏️ Майнить (+5 BTC)")
    print("2. ⌨️ Купить клавиатуру (5 BTC)")
    print("3. 🪑 Купить кресло (5 BTC)")
    print("4. 💣 Купить бомбу (5 BTC)")
    print("5. Назад")
    
    while True:
        choice = input(f"{CYAN}market> {RESET}")
        
        if choice == '1':
            balance += 5
            print(f"{GREEN}⛏️ Намайнено! Баланс: {balance} BTC{RESET}")
        elif choice == '2':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплена клавиатура!{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '3':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплено кресло!{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '4':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплена бомба! 💣{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '5':
            break

# ============================================================
#  🏗️ КОМНАТА BUILD
# ============================================================
def build_room():
    os.system('clear')
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════════╗
║{PURPLE}                  🏗️ КОМНАТА BUILD 🏗️                       {CYAN}║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║{YELLOW}  🖥️  Мониторы светятся.                                     {CYAN}║
║{YELLOW}  🐱  Феликс сидит на клавиатуре.                            {CYAN}║
║{YELLOW}  ☕  Чай стоит рядом.                                       {CYAN}║
║                                                              ║
║{GREEN}  Введи 'help' для списка команд.                            {CYAN}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")
    
    build_config = {
        'name': 'MyOS',
        'theme': 'dark',
        'wallpaper': 'cosmos',
        'memes': 'on',
        'code': ''
    }
    
    while True:
        cmd = input(f"{PURPLE}build> {RESET}").strip().lower()
        
        if cmd == "help":
            print(f"""{YELLOW}
📋 КОМАНДЫ BUILD:

  distributiv       — начать сборку
  theme [название]  — выбрать тему
  wallpaper [имя]   — выбрать обои
  memes [on/off]    — мемы
  code add          — добавить код
  create            — собрать дистрибутив
  run               — запустить собранное
  felix             — позвать Феликса
  back              — выйти из комнаты
{RESET}""")
        
        elif cmd == "distributiv":
            name = input("Название дистрибутива: ").strip()
            build_config['name'] = name
            print(f"{GREEN}📦 Дистрибутив: {name}{RESET}")
        
        elif cmd.startswith("theme "):
            theme = cmd.split(" ", 1)[1]
            build_config['theme'] = theme
            print(f"{GREEN}🎨 Тема: {theme}{RESET}")
        
        elif cmd.startswith("wallpaper "):
            wp = cmd.split(" ", 1)[1]
            build_config['wallpaper'] = wp
            print(f"{GREEN}🖼️ Обои: {wp}{RESET}")
        
        elif cmd.startswith("memes "):
            mem = cmd.split(" ", 1)[1]
            build_config['memes'] = mem
            print(f"{GREEN}😂 Мемы: {mem}{RESET}")
        
        elif cmd == "code add":
            code = input("Введи свой код: ")
            build_config['code'] += code + "\n"
            print(f"{GREEN}💻 Код добавлен!{RESET}")
        
        elif cmd == "create":
            print(f"{YELLOW}📦 Сборка...{RESET}")
            time.sleep(1)
            build_file = os.path.expanduser(f"~/{build_config['name']}.py")
            with open(build_file, "w") as f:
                f.write(f"#!/usr/bin/env python3\n")
                f.write(f"# {build_config['name']} — собран в FeliksOS Build\n")
                f.write(f"# Тема: {build_config['theme']}\n")
                f.write(f"# Обои: {build_config['wallpaper']}\n")
                f.write(f"# Мемы: {build_config['memes']}\n\n")
                f.write(build_config['code'])
                f.write(f"\nprint('🐱 {build_config['name']} работает!')\n")
            print(f"{GREEN}✅ Дистрибутив {build_config['name']} собран!{RESET}")
            print(f"{CYAN}📂 Файл: {build_file}{RESET}")
        
        elif cmd == "run":
            build_file = os.path.expanduser(f"~/{build_config['name']}.py")
            if os.path.exists(build_file):
                os.system(f"python3 {build_file}")
            else:
                print(f"{RED}❌ Сначала собери дистрибутив (create){RESET}")
        
        elif cmd == "felix":
            print(f"{CYAN}{CAT}{RESET}")
            print(f"{YELLOW}🐱 Феликс: «Я в комнате build! Собирай!»{RESET}")
        
        elif cmd == "back":
            print(f"{YELLOW}🚪 Выход из комнаты build...{RESET}")
            break
        else:
            print(f"{RED}Неизвестная команда. Введи 'help'.{RESET}")

# ============================================================
#  ➕ ДОБАВЛЕНИЕ КОМАНД
# ============================================================
def add_command():
    print(f"{YELLOW}➕ Добавление новой команды{RESET}")
    name = input("Название команды: ").strip()
    code = input("Код Python: ").strip()
    
    with open(os.path.expanduser("~/feliksos_custom.py"), "a") as f:
        f.write(f"\n# Команда: {name}\n{code}\n")
    
    print(f"{GREEN}✅ Команда '{name}' добавлена!{RESET}")
    print(f"{CYAN}Она сохранена в ~/feliksos_custom.py{RESET}")

# ============================================================
#  📜 ЛОР FELIKSOS
# ============================================================
def lore():
    print(f"""{YELLOW}
📜 ЛОР FELIKSOS:

🐱 FeliksOS — это вселенная.
🧠 Kernel (ты) — создатель.
🐱 Феликс — душа, кот.
🐈 Пушок — напарник, серый кот.

👥 КОМАНДА:
  404Feliks — искатель секретов
  Yiming — технический гений
  Misha/Bebrik — тестировщик
  Night — ночная смена
  Mimic — новичок-ветеран

💀 C0NSHI — бывший злодей.
🪳 НИЛ — создатель _pw, тараканов.

📦 ДИСТРИБУТИВЫ:
  Farch, Torham, Fubuntu, Felululuntu, Felililintu...

🖤 Всё началось с кота.
{RESET}""")

# ============================================================
#  🎨 СМЕНА ТЕМЫ
# ============================================================
def change_theme():
    print(f"{YELLOW}🎨 Смена темы{RESET}")
    print("1. Тёмная")
    print("2. Космос")
    print("3. Кот")
    print("4. Назад")
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == "1":
        print(f"{GREEN}🖤 Тема: Тёмная{RESET}")
    elif choice == "2":
        print(f"{GREEN}🌌 Тема: Космос{RESET}")
    elif choice == "3":
        print(f"{GREEN}🐱 Тема: Кот{RESET}")

# ============================================================
#  🖼️ СМЕНА ОБОЕВ
# ============================================================
def change_wallpaper():
    print(f"{YELLOW}🖼️ Смена обоев{RESET}")
    print("1. Космос")
    print("2. Кот")
    print("3. Звёзды")
    print("4. Назад")
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == "1":
        show_wallpaper()
    elif choice == "2":
        print(f"{CYAN}{CAT}{RESET}")
    elif choice == "3":
        cosmos_animation()

# ============================================================
#  🚀 ГЛАВНАЯ ФУНКЦИЯ
# ============================================================
def main():
    show_wallpaper()
    print(f"{GREEN}Добро пожаловать в FeliksOS Mobile v1.5!{RESET}")
    print(f"{GREEN}Введи 'help' для списка команд.{RESET}\n")
    
    while True:
        try:
            cmd = input(f"{CYAN}feliksos> {RESET}").strip().lower()
            
            if cmd == "help":
                show_help()
            elif cmd == "version":
                print(f"{GREEN}FeliksOS Mobile v1.5{RESET}")
            elif cmd == "meow":
                print(f"{YELLOW}🐱 Мяу!{RESET}")
            elif cmd == "cat":
                print(f"{CYAN}{CAT}{RESET}")
            elif cmd == "cats":
                cats_info()
            elif cmd == "felix":
                felix_info()
            elif cmd == "calc":
                calculator()
            elif cmd == "random":
                random_number()
            elif cmd == "timer":
                timer()
            elif cmd == "date":
                show_date()
            elif cmd == "notes":
                notes()
            elif cmd == "system":
                system_info()
            elif cmd == "game":
                guess_game()
            elif cmd == "ceasar":
                ceasar_cipher()
            elif cmd == "cosmos":
                cosmos_animation()
            elif cmd == "market":
                market()
            elif cmd == "build":
                build_room()
            elif cmd == "addcmd":
                add_command()
            elif cmd == "lore":
                lore()
            elif cmd == "theme":
                change_theme()
            elif cmd == "wallpaper":
                change_wallpaper()
            elif cmd == "clear":
                show_wallpaper()
            elif cmd == "exit":
                print(f"{YELLOW}🐱 Феликс: Пока, Kernel!{RESET}")
                break
            else:
                print(f"{RED}Неизвестная команда. Введи 'help'.{RESET}")
        except KeyboardInterrupt:
            print(f"\n{YELLOW}🐱 Феликс: Пока!{RESET}")
            break

# ============================================================
if __name__ == "__main__":
    main()#!/usr/bin/env python3
# ============================================================
#  🐱 FELIKSOS MOBILE v1.5
#  📱 Terminal Edition for UserLAnd
#  🖤 Created by Kernel
# ============================================================

import os
import sys
import time
import random
from datetime import datetime, timedelta

# ============================================================
#  🎨 ЦВЕТА
# ============================================================
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'

# ============================================================
#  🐱 ASCII-КОТ
# ============================================================
CAT = r"""
      /\_/\
     ( o.o )
      > ^ <
"""

# ============================================================
#  🌌 КОСМИЧЕСКИЕ ОБОИ
# ============================================================
def show_wallpaper():
    os.system('clear')
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════════╗
║{PURPLE}                    🌌 КОСМОС FELIKSOS 🌌                    {CYAN}║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║{YELLOW}        *        .        ✦        .        *                {CYAN}║
║{WHITE}     .        *        .        🌟        .        *          {CYAN}║
║{PURPLE}         ✦        🌌        .        ✦        .               {CYAN}║
║                                                              ║
║{BLUE}              🪐  ПЛАНЕТЫ  🪐  ЗВЁЗДЫ  🪐  КОСМОС              {CYAN}║
║                                                              ║
║{YELLOW}        .        *        ✦        .        *                {CYAN}║
║{WHITE}     *        .        🌟        .        *        .          {CYAN}║
║{PURPLE}         .        ✦        .        🌌        ✦               {CYAN}║
║                                                              ║
║{CYAN}                  🐱 FELIKSOS MOBILE v1.5 🐱                  {CYAN}║
║                                                              ║
║{YELLOW}              Добро пожаловать, Kernel!                       {CYAN}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")

# ============================================================
#  📋 СПРАВКА
# ============================================================
def show_help():
    print(f"""{YELLOW}
📋 ДОСТУПНЫЕ КОМАНДЫ:

  ОСНОВНЫЕ:
  help      — этот список
  version   — версия FeliksOS
  meow      — Феликс мяукает
  cat       — ASCII-кот
  cats      — Феликс и Пушок
  felix     — информация о Феликсе
  clear     — очистить экран
  exit      — выход

  ИНСТРУМЕНТЫ:
  calc      — калькулятор
  random    — случайное число
  timer     — таймер
  date      — дата и время
  notes     — заметки
  system    — информация о системе

  ИГРЫ И РАЗВЛЕЧЕНИЯ:
  game      — игра "Угадай число"
  ceasar    — шифр Цезаря
  cosmos    — анимация космоса
  market    — магазин FeliksOS

  НОВОЕ:
  build     — комната сборки
  addcmd    — добавить команду
  lore      — лор FeliksOS
  theme     — смена темы
  wallpaper — смена обоев
{RESET}""")

# ============================================================
#  🧮 КАЛЬКУЛЯТОР
# ============================================================
def calculator():
    print(f"{YELLOW}🧮 Калькулятор FeliksOS{RESET}")
    print("Введи выражение (например: 2 + 2)")
    print("Или 'back' для возврата.")
    
    while True:
        expr = input(f"{CYAN}calc> {RESET}").strip()
        if expr.lower() == 'back':
            break
        try:
            result = eval(expr)
            print(f"{GREEN}Результат: {result}{RESET}")
        except:
            print(f"{RED}Ошибка! Попробуй снова.{RESET}")

# ============================================================
#  🎲 СЛУЧАЙНОЕ ЧИСЛО
# ============================================================
def random_number():
    print(f"{YELLOW}🎲 Случайное число{RESET}")
    try:
        min_num = int(input("Минимум: "))
        max_num = int(input("Максимум: "))
        result = random.randint(min_num, max_num)
        print(f"{GREEN}🎲 Выпало: {result}{RESET}")
    except:
        print(f"{RED}Ошибка! Введи числа.{RESET}")

# ============================================================
#  ⏰ ТАЙМЕР
# ============================================================
def timer():
    print(f"{YELLOW}⏰ Таймер{RESET}")
    try:
        seconds = int(input("Секунды: "))
        print(f"{CYAN}⏳ Отсчёт пошёл...{RESET}")
        for i in range(seconds, 0, -1):
            print(f"\r{CYAN}Осталось: {i} сек{RESET}", end="")
            time.sleep(1)
        print(f"\n{GREEN}⏰ Время вышло!{RESET}")
    except:
        print(f"{RED}Ошибка! Введи число.{RESET}")

# ============================================================
#  📅 ДАТА И ВРЕМЯ (МСК)
# ============================================================
def show_date():
    now = datetime.now() + timedelta(hours=3)  # МСК
    print(f"{GREEN}📅 Дата: {now.strftime('%d.%m.%Y')}{RESET}")
    print(f"{GREEN}🕐 Время: {now.strftime('%H:%M:%S')} (МСК){RESET}")

# ============================================================
#  📝 ЗАМЕТКИ
# ============================================================
def notes():
    print(f"{YELLOW}📝 Заметки{RESET}")
    print("1. Показать заметки")
    print("2. Добавить заметку")
    print("3. Назад")
    
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == '1':
        try:
            with open(os.path.expanduser("~/feliksos_notes.txt"), "r") as f:
                print(f"{GREEN}{f.read()}{RESET}")
        except:
            print(f"{RED}Заметок пока нет.{RESET}")
    elif choice == '2':
        note = input("Заметка: ")
        with open(os.path.expanduser("~/feliksos_notes.txt"), "a") as f:
            f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M')}] {note}\n")
        print(f"{GREEN}✅ Заметка добавлена!{RESET}")

# ============================================================
#  📊 ИНФОРМАЦИЯ О СИСТЕМЕ
# ============================================================
def system_info():
    print(f"{YELLOW}📊 Информация о системе{RESET}")
    print(f"{GREEN}📱 ОС: FeliksOS Mobile v1.5{RESET}")
    print(f"{GREEN}🐧 Платформа: Debian (UserLAnd){RESET}")
    print(f"{GREEN}🐍 Python: {sys.version.split()[0]}{RESET}")
    print(f"{GREEN}📂 Домашняя папка: {os.path.expanduser('~')}{RESET}")

# ============================================================
#  🐱 ИНФОРМАЦИЯ О ФЕЛИКСЕ
# ============================================================
def felix_info():
    print(f"{CYAN}{CAT}{RESET}")
    print(f"{YELLOW}🐱 Феликс{RESET}")
    print(f"{GREEN}Роль: Дух FeliksOS{RESET}")
    print(f"{GREEN}Характер: Спокойный, загадочный, независимый{RESET}")
    print(f"{GREEN}Любит: Спать, гулять, наблюдать за хаосом{RESET}")
    print(f"{GREEN}Статус: Легенда{RESET}")

# ============================================================
#  🐱 ФЕЛИКС И ПУШОК
# ============================================================
def cats_info():
    print(f"{CYAN}{CAT}{RESET}")
    print(f"{YELLOW}🐱 Феликс{RESET}")
    print(f"{GREEN}Главный кот. Символ FeliksOS. Загадочный.{RESET}")
    print(f"{YELLOW}🐈 Пушок{RESET}")
    print(f"{GREEN}Серый напарник. Хранитель уюта. Спит на кровати.{RESET}")
    print(f"{PURPLE}Вместе — команда. Вместе — FeliksOS.{RESET}")

# ============================================================
#  🎮 ИГРА: УГАДАЙ ЧИСЛО
# ============================================================
def guess_game():
    print(f"{YELLOW}🎮 Угадай число!{RESET}")
    print("Я загадал число от 1 до 100.")
    
    secret = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input(f"{CYAN}Твой вариант: {RESET}"))
            attempts += 1
            
            if guess < secret:
                print(f"{BLUE}Больше!{RESET}")
            elif guess > secret:
                print(f"{BLUE}Меньше!{RESET}")
            else:
                print(f"{GREEN}🎉 Угадал! С {attempts} попыток!{RESET}")
                break
        except:
            print(f"{RED}Введи число!{RESET}")

# ============================================================
#  🔐 ШИФР ЦЕЗАРЯ
# ============================================================
def ceasar_cipher():
    print(f"{YELLOW}🔐 Шифр Цезаря{RESET}")
    print("1. Зашифровать")
    print("2. Расшифровать")
    print("3. Назад")
    
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == '1':
        text = input("Текст: ")
        shift = int(input("Сдвиг: "))
        result = ''.join(chr((ord(c) + shift) % 256) for c in text)
        print(f"{GREEN}Зашифровано: {result}{RESET}")
    elif choice == '2':
        text = input("Текст: ")
        shift = int(input("Сдвиг: "))
        result = ''.join(chr((ord(c) - shift) % 256) for c in text)
        print(f"{GREEN}Расшифровано: {result}{RESET}")

# ============================================================
#  🌌 КОСМОС (АНИМАЦИЯ)
# ============================================================
def cosmos_animation():
    stars = ['*', '.', '✦', '🌟', '✨', '·']
    for i in range(30):
        os.system('clear')
        print(f"{CYAN}🌌 КОСМОС FELIKSOS 🌌{RESET}\n")
        for _ in range(15):
            line = ''.join(random.choice(stars) if random.random() > 0.7 else ' ' for _ in range(60))
            print(f"{random.choice([CYAN, BLUE, PURPLE, WHITE])}{line}{RESET}")
        time.sleep(0.3)

# ============================================================
#  🛒 МАГАЗИН
# ============================================================
def market():
    balance = 0
    
    print(f"{YELLOW}🛒 FELIKSOS MARKET{RESET}")
    print(f"💰 Баланс: {balance} BTC")
    print("\n1. ⛏️ Майнить (+5 BTC)")
    print("2. ⌨️ Купить клавиатуру (5 BTC)")
    print("3. 🪑 Купить кресло (5 BTC)")
    print("4. 💣 Купить бомбу (5 BTC)")
    print("5. Назад")
    
    while True:
        choice = input(f"{CYAN}market> {RESET}")
        
        if choice == '1':
            balance += 5
            print(f"{GREEN}⛏️ Намайнено! Баланс: {balance} BTC{RESET}")
        elif choice == '2':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплена клавиатура!{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '3':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплено кресло!{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '4':
            if balance >= 5:
                balance -= 5
                print(f"{GREEN}✅ Куплена бомба! 💣{RESET}")
            else:
                print(f"{RED}❌ Недостаточно BTC!{RESET}")
        elif choice == '5':
            break

# ============================================================
#  🏗️ КОМНАТА BUILD
# ============================================================
def build_room():
    os.system('clear')
    print(f"""{CYAN}
╔══════════════════════════════════════════════════════════════╗
║{PURPLE}                  🏗️ КОМНАТА BUILD 🏗️                       {CYAN}║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║{YELLOW}  🖥️  Мониторы светятся.                                     {CYAN}║
║{YELLOW}  🐱  Феликс сидит на клавиатуре.                            {CYAN}║
║{YELLOW}  ☕  Чай стоит рядом.                                       {CYAN}║
║                                                              ║
║{GREEN}  Введи 'help' для списка команд.                            {CYAN}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{RESET}
""")
    
    build_config = {
        'name': 'MyOS',
        'theme': 'dark',
        'wallpaper': 'cosmos',
        'memes': 'on',
        'code': ''
    }
    
    while True:
        cmd = input(f"{PURPLE}build> {RESET}").strip().lower()
        
        if cmd == "help":
            print(f"""{YELLOW}
📋 КОМАНДЫ BUILD:

  distributiv       — начать сборку
  theme [название]  — выбрать тему
  wallpaper [имя]   — выбрать обои
  memes [on/off]    — мемы
  code add          — добавить код
  create            — собрать дистрибутив
  run               — запустить собранное
  felix             — позвать Феликса
  back              — выйти из комнаты
{RESET}""")
        
        elif cmd == "distributiv":
            name = input("Название дистрибутива: ").strip()
            build_config['name'] = name
            print(f"{GREEN}📦 Дистрибутив: {name}{RESET}")
        
        elif cmd.startswith("theme "):
            theme = cmd.split(" ", 1)[1]
            build_config['theme'] = theme
            print(f"{GREEN}🎨 Тема: {theme}{RESET}")
        
        elif cmd.startswith("wallpaper "):
            wp = cmd.split(" ", 1)[1]
            build_config['wallpaper'] = wp
            print(f"{GREEN}🖼️ Обои: {wp}{RESET}")
        
        elif cmd.startswith("memes "):
            mem = cmd.split(" ", 1)[1]
            build_config['memes'] = mem
            print(f"{GREEN}😂 Мемы: {mem}{RESET}")
        
        elif cmd == "code add":
            code = input("Введи свой код: ")
            build_config['code'] += code + "\n"
            print(f"{GREEN}💻 Код добавлен!{RESET}")
        
        elif cmd == "create":
            print(f"{YELLOW}📦 Сборка...{RESET}")
            time.sleep(1)
            build_file = os.path.expanduser(f"~/{build_config['name']}.py")
            with open(build_file, "w") as f:
                f.write(f"#!/usr/bin/env python3\n")
                f.write(f"# {build_config['name']} — собран в FeliksOS Build\n")
                f.write(f"# Тема: {build_config['theme']}\n")
                f.write(f"# Обои: {build_config['wallpaper']}\n")
                f.write(f"# Мемы: {build_config['memes']}\n\n")
                f.write(build_config['code'])
                f.write(f"\nprint('🐱 {build_config['name']} работает!')\n")
            print(f"{GREEN}✅ Дистрибутив {build_config['name']} собран!{RESET}")
            print(f"{CYAN}📂 Файл: {build_file}{RESET}")
        
        elif cmd == "run":
            build_file = os.path.expanduser(f"~/{build_config['name']}.py")
            if os.path.exists(build_file):
                os.system(f"python3 {build_file}")
            else:
                print(f"{RED}❌ Сначала собери дистрибутив (create){RESET}")
        
        elif cmd == "felix":
            print(f"{CYAN}{CAT}{RESET}")
            print(f"{YELLOW}🐱 Феликс: «Я в комнате build! Собирай!»{RESET}")
        
        elif cmd == "back":
            print(f"{YELLOW}🚪 Выход из комнаты build...{RESET}")
            break
        else:
            print(f"{RED}Неизвестная команда. Введи 'help'.{RESET}")

# ============================================================
#  ➕ ДОБАВЛЕНИЕ КОМАНД
# ============================================================
def add_command():
    print(f"{YELLOW}➕ Добавление новой команды{RESET}")
    name = input("Название команды: ").strip()
    code = input("Код Python: ").strip()
    
    with open(os.path.expanduser("~/feliksos_custom.py"), "a") as f:
        f.write(f"\n# Команда: {name}\n{code}\n")
    
    print(f"{GREEN}✅ Команда '{name}' добавлена!{RESET}")
    print(f"{CYAN}Она сохранена в ~/feliksos_custom.py{RESET}")

# ============================================================
#  📜 ЛОР FELIKSOS
# ============================================================
def lore():
    print(f"""{YELLOW}
📜 ЛОР FELIKSOS:

🐱 FeliksOS — это вселенная.
🧠 Kernel (ты) — создатель.
🐱 Феликс — душа, кот.
🐈 Пушок — напарник, серый кот.

👥 КОМАНДА:
  404Feliks — искатель секретов
  Yiming — технический гений
  Misha/Bebrik — тестировщик
  Night — ночная смена
  Mimic — новичок-ветеран

💀 C0NSHI — бывший злодей.
🪳 НИЛ — создатель _pw, тараканов.

📦 ДИСТРИБУТИВЫ:
  Farch, Torham, Fubuntu, Felululuntu, Felililintu...

🖤 Всё началось с кота.
{RESET}""")

# ============================================================
#  🎨 СМЕНА ТЕМЫ
# ============================================================
def change_theme():
    print(f"{YELLOW}🎨 Смена темы{RESET}")
    print("1. Тёмная")
    print("2. Космос")
    print("3. Кот")
    print("4. Назад")
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == "1":
        print(f"{GREEN}🖤 Тема: Тёмная{RESET}")
    elif choice == "2":
        print(f"{GREEN}🌌 Тема: Космос{RESET}")
    elif choice == "3":
        print(f"{GREEN}🐱 Тема: Кот{RESET}")

# ============================================================
#  🖼️ СМЕНА ОБОЕВ
# ============================================================
def change_wallpaper():
    print(f"{YELLOW}🖼️ Смена обоев{RESET}")
    print("1. Космос")
    print("2. Кот")
    print("3. Звёзды")
    print("4. Назад")
    choice = input(f"{CYAN}Выбор: {RESET}")
    
    if choice == "1":
        show_wallpaper()
    elif choice == "2":
        print(f"{CYAN}{CAT}{RESET}")
    elif choice == "3":
        cosmos_animation()

# ============================================================
#  🚀 ГЛАВНАЯ ФУНКЦИЯ
# ============================================================
def main():
    show_wallpaper()
    print(f"{GREEN}Добро пожаловать в FeliksOS Mobile v1.5!{RESET}")
    print(f"{GREEN}Введи 'help' для списка команд.{RESET}\n")
    
    while True:
        try:
            cmd = input(f"{CYAN}feliksos> {RESET}").strip().lower()
            
            if cmd == "help":
                show_help()
            elif cmd == "version":
                print(f"{GREEN}FeliksOS Mobile v1.5{RESET}")
            elif cmd == "meow":
                print(f"{YELLOW}🐱 Мяу!{RESET}")
            elif cmd == "cat":
                print(f"{CYAN}{CAT}{RESET}")
            elif cmd == "cats":
                cats_info()
            elif cmd == "felix":
                felix_info()
            elif cmd == "calc":
                calculator()
            elif cmd == "random":
                random_number()
            elif cmd == "timer":
                timer()
            elif cmd == "date":
                show_date()
            elif cmd == "notes":
                notes()
            elif cmd == "system":
                system_info()
            elif cmd == "game":
                guess_game()
            elif cmd == "ceasar":
                ceasar_cipher()
            elif cmd == "cosmos":
                cosmos_animation()
            elif cmd == "market":
                market()
            elif cmd == "build":
                build_room()
            elif cmd == "addcmd":
                add_command()
            elif cmd == "lore":
                lore()
            elif cmd == "theme":
                change_theme()
            elif cmd == "wallpaper":
                change_wallpaper()
            elif cmd == "clear":
                show_wallpaper()
            elif cmd == "exit":
                print(f"{YELLOW}🐱 Феликс: Пока, Kernel!{RESET}")
                break
            else:
                print(f"{RED}Неизвестная команда. Введи 'help'.{RESET}")
        except KeyboardInterrupt:
            print(f"\n{YELLOW}🐱 Феликс: Пока!{RESET}")
            break

# ============================================================
if __name__ == "__main__":
    main()
