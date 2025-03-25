import math

# Введення значень x та b
x = float(input("Введіть значення 'x': "))
b = float(input("Введіть значення 'b': "))

if b == 0:
    print("Помилка: b не може бути 0.")
else:
    # Основні Обчислення
    if b < 0:
        print("Помилка: b має бути >= 0.")
    else:
        a = b**3 + math.log(abs(b))
        c = a**2 + math.sqrt(b)
        y = math.exp(x) + 5.8**c
        print(f"Значення виразу = {y:.2f}")
