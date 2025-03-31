def get_student():
    students = [
        "Пожоджук Володимир Романович",
        "Храбатин Ярослав Володимирович",
        "Волошин Володимир Михайлович",
        "Коржик Михайло Михайлович"
    ]

    num = int(input(f"Введіть номер студента (1-{len(students)}): ")) - 1
    if 0 <= num < len(students):
        print("Студент:", students[num])
    else:
        print(f"Недійсний номер! Тільки від 1 до {len(students)}")


def get_train():
    routes = [
        "Івано-Франківськ - Львів",
        "Львів - Тернопіль",
        "Тернопіль - Ужгород",
        "Ужгород - Луцьк"
    ]

    num = int(input(f"Введіть номер поїзда (1-{len(routes)}): ")) - 1
    if 0 <= num < len(routes):
        print("Поїзд:", routes[num])
    else:
        print(f"Недійсний номер! Тільки від 1 до {len(routes)}")


def get_weekday():
    days = [
        "Понеділок - Monday",
        "Вівторок - Tuesday",
        "Середа - Wednesday",
        "Четвер - Thursday",
        "П'ятниця - Friday",
        "Субота - Saturday",
        "Неділя - Sunday"
    ]

    num = int(input(f"Введіть номер дня тижня (1-{len(days)}): ")) - 1
    if 0 <= num < len(days):
        print("День:", days[num])
    else:
        print(f"Недійсний номер! Тільки від 1 до {len(days)}")


def get_month_days():
    num = input("Введіть номер місяця (1-12): ")

    if num in ("1", "3", "5", "7", "8", "10", "12"):
        print("31 день")
    elif num in ("4", "6", "9", "11"):
        print("30 днів")
    elif num == "2":
        print("28-29 днів")
    else:
        print("Недійсний номер місяця! Тільки від 1 до 12")


def get_traffic_light():
    color = input("Введіть колір світлофора (червоний, жовтий, зелений): ").lower()

    if color == "червоний":
        print("Червоний - стояти")
    elif color == "жовтий":
        print("Жовтий - приготуватись до руху")
    elif color == "зелений":
        print("Зелений - рушати")
    else:
        print("Некоректний колір! Введіть червоний, жовтий або зелений")


print("\nОберіть завдання:")
print("1. Вибрати студента")
print("2. Вибрати поїзд")
print("3. Вибрати день тижня")
print("4. Дізнатись кількість днів у місяці")
print("5. Дізнатись дію світлофора")

choice = input("Введіть номер завдання: ")

if choice == "1":
    get_student()
elif choice == "2":
    get_train()
elif choice == "3":
    get_weekday()
elif choice == "4":
    get_month_days()
elif choice == "5":
    get_traffic_light()
else:
    print("Некоректний вибір. Спробуйте ще раз.")
