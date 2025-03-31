import math, random, requests, json

# 1. Вік та право голосу
def task1():
    try:
        age = int(input("Введіть свій вік: "))
    except ValueError:
        print("Невірне значення віку.")
        return
    if age >= 18:
        print("Ви маєте право голосу.")
    else:
        years_left = 18 - age
        print(f"Ви зможете голосувати через {years_left} років.")

# 2. Координати двох точок – чи знаходяться вони на одному колі з центром (0,0)
def task2():
    try:
        x1 = float(input("Введіть x1: "))
        y1 = float(input("Введіть y1: "))
        x2 = float(input("Введіть x2: "))
        y2 = float(input("Введіть y2: "))
    except ValueError:
        print("Невірні координати.")
        return
    r1_sq = x1**2 + y1**2
    r2_sq = x2**2 + y2**2
    if math.isclose(r1_sq, r2_sq, rel_tol=1e-9):
        print("Точки знаходяться на одному колі з центром в (0,0).")
    else:
        print("Точки не лежать на одному колі з центром в (0,0).")

# 3. Знайти найменше та найбільше із трьох чисел
def task3():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        c = float(input("Введіть третє число: "))
    except ValueError:
        print("Невірне число.")
        return
    smallest = min(a, b, c)
    largest = max(a, b, c)
    print(f"Найменше число: {smallest}")
    print(f"Найбільше число: {largest}")

# 4. Чи пройде круг через квадрат?
def task4():
    try:
        r = float(input("Введіть радіус кола: "))
        a = float(input("Введіть довжину сторони квадрата: "))
    except ValueError:
        print("Невірне значення.")
        return
    if 2 * r <= a:
        print("Круг пройде через квадрат.")
    else:
        print("Круг не пройде через квадрат.")

# 5. Чи можна побудувати трикутник із трьох відрізків?
def task5():
    try:
        a = float(input("Введіть довжину першого відрізка: "))
        b = float(input("Введіть довжину другого відрізка: "))
        c = float(input("Введіть довжину третього відрізка: "))
    except ValueError:
        print("Невірне значення.")
        return
    if a <= 0 or b <= 0 or c <= 0:
        print("Довжини повинні бути додатні.")
        return
    if a < b + c and b < a + c and c < a + b:
        print("З цих відрізків можна побудувати трикутник.")
    else:
        print("З цих відрізків побудувати трикутник неможливо.")

# 6. Тип трикутника за двома кутами
def task6():
    try:
        angle1 = float(input("Введіть перший кут (в градусах): "))
        angle2 = float(input("Введіть другий кут (в градусах): "))
    except ValueError:
        print("Невірне значення кута.")
        return
    angle3 = 180 - (angle1 + angle2)
    if angle3 <= 0:
        print("Невірні кути, неможливо побудувати трикутник.")
        return
    # Перевірка на прямокутність
    if math.isclose(angle1, 90, rel_tol=1e-9) or math.isclose(angle2, 90, rel_tol=1e-9) or math.isclose(angle3, 90, rel_tol=1e-9):
        print("Трикутник прямокутний.")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Трикутник тупокутний.")
    else:
        print("Трикутник гострокутний.")

# 7. Тип трикутника за сторонами (рівносторонній, рівнобедрений, різносторонній)
def task7():
    try:
        a = float(input("Введіть довжину першої сторони: "))
        b = float(input("Введіть довжину другої сторони: "))
        c = float(input("Введіть довжину третьої сторони: "))
    except ValueError:
        print("Невірне значення сторони.")
        return
    if a <= 0 or b <= 0 or c <= 0:
        print("Сторони мають бути додатні.")
        return

    # Спочатку перевіримо, чи можна побудувати трикутник
    if a >= b + c or b >= a + c or c >= a + b:
        print("Задані відрізки не утворюють трикутник.")
        return
    if math.isclose(a, b) and math.isclose(b, c):
        print("Трикутник рівносторонній.")
    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        print("Трикутник рівнобедрений.")
    else:
        print("Трикутник різносторонній.")

# 8. Чи перетинаються два відрізки (на прямій)
def task8():
    try:
        print("Введіть координати першого відрізка:")
        x1 = float(input("x1: "))
        x2 = float(input("x2: "))
        print("Введіть координати другого відрізка:")
        x3 = float(input("x3: "))
        x4 = float(input("x4: "))
    except ValueError:
        print("Невірне значення координати.")
        return
    # Приведемо кінці до порядку
    seg1_min, seg1_max = min(x1, x2), max(x1, x2)
    seg2_min, seg2_max = min(x3, x4), max(x3, x4)

    # Результат
    if max(seg1_min, seg2_min) <= min(seg1_max, seg2_max):
        print("Відрізки перетинаються.")
    else:
        print("Відрізки не перетинаються.")

# 9. П'ять чисел: підрахувати кількість парних та чисел, кратних 3
def task9():
    nums = []
    for i in range(1, 6):
        try:
            n = int(input(f"Введіть число {i}: "))
            nums.append(n)
        except ValueError:
            print("Невірне значення, спробуйте ще раз.")
            return
    count_even = sum(1 for n in nums if n % 2 == 0)
    count_div3 = sum(1 for n in nums if n % 3 == 0)
    print(f"Кількість парних чисел: {count_even}")
    print(f"Кількість чисел, кратних 3: {count_div3}")

# 10. Переклад оцінки з п’ятибальної системи на університетську
def task10():
    try:
        grade = int(input("Введіть оцінку (1-5): "))
    except ValueError:
        print("Невірна оцінка.")
        return
    mapping = {
        5: "відмінно",
        4: "добре",
        3: "задовільно",
        2: "незадовільно",
        1: "незадовільно"}
    result = mapping.get(grade, "Невірна оцінка")
    print("Університетська оцінка:", result)

# 11. Розташування точки відносно кола з центром (0,0)
def task11():
    try:
        R = float(input("Введіть радіус кола R: "))
        x = float(input("Введіть координату x точки: "))
        y = float(input("Введіть координату y точки: "))
    except ValueError:
        print("Невірне значення.")
        return
    dist = math.sqrt(x**2 + y**2)
    if math.isclose(dist, R, rel_tol=1e-9):
        print("Точка знаходиться на колі.")
    elif dist < R:
        print("Точка знаходиться в середині кола.")
    else:
        print("Точка знаходиться за межами кола.")

# 12. Розташування точок відносно віток параболи
def task12():
    try:
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        c = float(input("Введіть c: "))
    except ValueError:
        print("Невірні коефіцієнти.")
        return

    # Обчислюємо дискримінант для знаходження коренів
    D = b**2 - 4*a*c
    if D < 0:
        print("Парабола не має перетину з віссю x, тому неможливо визначити 'вітки'.")
        return
    r1 = (-b - math.sqrt(D)) / (2*a)
    r2 = (-b + math.sqrt(D)) / (2*a)
    left, right = min(r1, r2), max(r1, r2)

    print(f"Корені рівняння: {left:.2f} та {right:.2f}")

    try:
        x1 = float(input("Введіть x координату першої точки: "))
        y1 = float(input("Введіть y координату першої точки: "))
        x2 = float(input("Введіть x координату другої точки: "))
        y2 = float(input("Введіть y координату другої точки: "))
    except ValueError:
        print("Невірні координати.")
        return

    pos1 = "між вітками" if left < x1 < right else "зовні віток"
    pos2 = "між вітками" if left < x2 < right else "зовні віток"

    # Результат
    if pos1 == pos2:
        print(f"Обидві точки {pos1}.")
    else:
        print("Точки розташовані по-різному щодо віток параболи.")

# 13. Який це трикутник за сторонами (рівносторонній, рівнобедрений, різносторонній)
def task13():
    try:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))
    except ValueError:
        print("Невірне значення сторони.")
        return
    if a <= 0 or b <= 0 or c <= 0:
        print("Сторони мають бути додатні.")
        return
    if a >= b + c or b >= a + c or c >= a + b:
        print("Відрізки не утворюють трикутник.")
        return
    if math.isclose(a, b) and math.isclose(b, c):
        print("Трикутник рівносторонній.")
    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        print("Трикутник рівнобедрений.")
    else:
        print("Трикутник різносторонній.")

# 14. Сума покупки зі знижкою
def task14():
    try:
        total = float(input("Введіть суму покупки (грн): "))
    except ValueError:
        print("Невірне значення.")
        return
    if total > 5000:
        discount = 0.20
    elif total > 1000:
        discount = 0.10
    else:
        discount = 0.0
    final_price = total * (1 - discount)
    print(f"Кінцева сума до сплати: {final_price:.2f} грн (знижка {discount*100:.0f}%)")

# 15. Курс гривні до валюти
def task15():
    currency = input("Введіть валюту (USD, EUR, GBP): ").strip().upper()
    try:
        value = requests.get(f"https://api.currencyapi.com/v3/latest?apikey=cur_live_AVoybm75kYcsX88g0nf8sZ6kZ48ID0HNdK7UIZn3&base_currency={currency}&currencies=UAH").json()["data"]["UAH"]["value"]
        print(f"Курс гривні до {currency}: {value:.2f} грн")
    except:
        print("Помилка. Невірна валюта або немає інтернет з'єднання.")

# 16. Камінь, ножиці, папір
def task16():
    choices = ["камінь", "ножиці", "папір"]
    user_choice = input("Введіть свій вибір (камінь, ножиці, папір): ").strip().lower()
    if user_choice not in choices:
        print("Невірний вибір.")
        return
    comp_choice = random.choice(choices)
    print(f"Комп'ютер вибрав: {comp_choice}")
    if user_choice == comp_choice:
        print("Нічия.")
    else:
        # Правила: камінь б'є ножиці, ножиці б'ють папір, папір б'є камінь.
        if (user_choice == "камінь" and comp_choice == "ножиці") or \
           (user_choice == "ножиці" and comp_choice == "папір") or \
           (user_choice == "папір" and comp_choice == "камінь"):
            print("Ви перемогли!")
        else:
            print("Переміг комп'ютер.")

# 17. Чи можна вийти, якщо температура і дощ
def task17():
    try:
        get = requests.get("https://api.weatherapi.com/v1/current.json?key=81fbc14aed424974b15105554253103&q=Ivano-Frankivsk,UA").json()
        print(f"Країна         : {get['location']['country']}")
        print(f"Область        : {get['location']['region']}")
        print(f"Температура    : {get['current']['temp_c']}°C")
        print(f"Вологість пов. : {get['current']['humidity']}%")
        print(f"Швидкість віт. : {get['current']['wind_kph']} км/год.")
        print(f"Тиск повітря   : {get['current']['pressure_mb']} mbar")
        if get['current']['is_day'] == 1:
            print(f"Чи день?       : Так")
        else:
            print(f"Чи день?       : Ні")
        if "rain" in get['current']['condition']['text']:
            print(f"Чи йде дощ?    : Можливо")
        else:
            print(f"Чи йде дощ?    : Ні")
        if get['current']['temp_c'] > 5 and get['current']['is_day'] == 1 and "rain" not in get['current']['condition']['text']:
            print(f"\033[01;31mМожна виходити\033[0m")
        else:
            print(f"\033[01;31mКраще не виходити\033[0m")
    except:
        print("Помилка. Немає інтернет з'єднання.")

tasks = {
    "1": ("Право голосу", task1),
    "2": ("Точки на одному колі", task2),
    "3": ("Найменше та найбільше із трьох чисел", task3),
    "4": ("Круг і квадрат", task4),
    "5": ("Можна побудувати трикутник?", task5),
    "6": ("Тип трикутника за кутами", task6),
    "7": ("Тип трикутника за сторонами", task7),
    "8": ("Перетин двох відрізків", task8),
    "9": ("П’ять чисел: парні та кратні 3", task9),
    "10": ("Переклад оцінки", task10),
    "11": ("Точка відносно кола", task11),
    "12": ("Точки відносно віток параболи", task12),
    "13": ("Тип трикутника (сторони)", task13),
    "14": ("Сума покупки зі знижкою", task14),
    "15": ("Курс валюти", task15),
    "16": ("Камінь, ножиці, папір", task16),
    "17": ("Чи можна виходити", task17)
}

for key in tasks:
    print(f"{key}. {tasks[key][0]}")

choice = input("Ваш вибір (1-17): ").strip()
task = tasks.get(choice)
if task:
    print("")
    task[1]()
else:
    print("Невірний вибір.")
