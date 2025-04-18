import math

# Зчитування відомого катета та гіпотенузи
a = float(input("Введіть довжину катета: "))
c = float(input("Введіть довжину гіпотенузи: "))

# Перевірка, чи гіпотенуза більше відомого катета
if c <= a:
    print("Гіпотенуза має бути більшою за катет.")
else:
    # Обчислення іншого катета за теоремою Піфагора
    b = math.sqrt(c**2 - a**2)

    # Обчислення площі прямокутного трикутника
    S = 0.5 * a * b

    # Виведення результатів
    print(f"Інший катет = {b:.2f}")
    print(f"Площа трикутника = {S:.2f}")
