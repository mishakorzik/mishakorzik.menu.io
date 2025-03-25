import math

# Введення значення 'x'
x = float(input("Введіть значення 'x': "))

# Перевірка знаменників
if x == 0:
    print("Помилка: x не може бути 0.")
elif math.cos(2 * x) + x**2 == 0:
    print("Помилка: Ділення на нуль, бо cos(2x) + x2 = 0.")
else:
    # Обчислення log(x)
    ln_x2 = math.log(x**2)

    # Обчислення cos(x)
    cos2x = math.cos(x)**2

    # Основні обчислення
    fraction1 = (ln_x2 + cos2x) / (math.cos(2 * x) + x**2)
    cube_root = x**(1/3)
    fraction2 = cube_root / x

    y = fraction1 + fraction2
    print("Значення виразу = {y:.2f}")
