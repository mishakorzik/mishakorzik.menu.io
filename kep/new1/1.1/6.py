import math

# Введення значення 'x'
x = float(input("Введіть значення 'x': "))

# Перевірка: для √x потрібно, щоб x > 0
if x <= 0:
    print("Помилка: x має бути більше 0")
elif math.cos(x)**2 + x**2 == 0:
    print("Помилка: Ділення на нуль")
else:
    # Основні обчислення
    term1 = (2 * x + math.sin(x)) / (math.cos(x)**2 + x**2)
    term2 = (0.5 ** x) / math.sqrt(x)

    y = term1 + term2
    print(f"Значення першого виразу = {y:.2f}")
