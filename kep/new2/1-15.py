def calc(variant, x):
    if variant == 1:
        if x < 0:
            return x**2 + 1
        elif 0 <= x < 2:
            return x**2 - 1
        else:
            return x
    elif variant == 2:
        if x <= -8:
            return 6*x**3 - 8
        elif -8 < x < 0:
            return x**3 - 8
        else:
            return 2*x**2
    elif variant == 3:
        if x <= -5:
            return 6*x + 8
        elif -5 < x <= 3:
            return x - 2
        else:
            return 2*x**2
    elif variant == 4:
        if x <= -4:
            return 2*x - 1
        elif -4 < x <= 5:
            return x**2 + 2
        else:
            return x + 3
    elif variant == 5:
        if x <= -8:
            return 6*x**3 - 8
        elif -8 < x < 0:
            return x**3 - 8
        else:
            return 2*x**2
    elif variant == 6:
        if x <= -1:
            return 2*x**3 + 3*x
        elif -1 < x < 0:
            return x**2 - 4
        else:
            return x**3
    elif variant == 7:
        if x <= -12:
            return 4*x**2 + 2*x
        elif -12 < x < 3:
            return 2*x**2 + 2*x
        else:
            return x + 1
    elif variant == 8:
        if x <= -4:
            return x**3 - 1
        elif -4 < x <= 3:
            return 2*x - 1
        else:
            return 3*x**3
    elif variant == 9:
        if x <= -2:
            return 4*x + 3
        elif -2 < x < 4:
            return 2*x**2 - 4
        else:
            return x**2 - 2
    elif variant == 10:
        if x <= -1:
            return 2*x + 4
        elif -1 < x < 0:
            return x - 4
        else:
            return x**3 + 4
    elif variant == 11:
        if x < -2:
            return 4*x**2 + 2*x
        elif -2 <= x < 3:
            return 2*x - 1
        else:
            return x**3 + 3
    elif variant == 12:
        if x < -3:
            return 3*x**2 + 2*x
        elif -3 <= x < 8:
            return 2*x + 1
        else:
            return 3*x
    elif variant == 13:
        if x <= -4:
            return 4*x + 2
        elif -4 < x < 2:
            return x - 2
        else:
            return x + 2
    elif variant == 14:
        if x <= -6:
            return 27*x + 3
        elif -6 < x < 3:
            return x**3 - 1
        else:
            return x**2 + 1
    elif variant == 15:
        if x <= -2:
            return x**3 + 2*x**2
        elif -2 < x < 3:
            return x**2 - 1
        else:
            return 2*x + 2
    else:
        return None

try:
    # Номер завдання
    v = int(input("Введіть номер варіанта (1-15): "))

    # Значення х
    x = float(input("Введіть знкчення x: "))

    # Обчислення
    result = calc(v, x)

    # Результат
    if result is None:
        print("Невідомий варіант.")
    else:
        print(f"Результат y = {result:.2f}")
except ValueError:
    print("Введіть коректні числа!")
