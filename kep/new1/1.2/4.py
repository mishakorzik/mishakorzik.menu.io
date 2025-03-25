import math

# Введення значень 'x' та 't'
x = float(input("Введіть значення x: "))
t = float(input("Введіть значення t: "))

if x <= 0:
    print("Помилка: x має бути більше 0.")
else:
    # Основні обчислення
    a = math.log10(x)
    b = math.sqrt(x**2 + t**2)

    y = abs(a - b)**(1/3)
    print(f"Значення виразу = {y:.2f}")
