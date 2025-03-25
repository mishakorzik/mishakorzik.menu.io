import math

# Введення значень x та p
x = float(input("Введіть значення x: "))
p = float(input("Введіть значення p: "))

a = math.exp(math.sqrt(abs(x)))
b = (math.sin(p)**2 + x**3)

if b == 0:
    print("Помилка: Ділення на нуль, оскільки b дорівнює 0.")
else:
    # Основні обчислення
    y = (a**3) / (b**2)

    print(f"Значення виразу = {y:.2f}")
