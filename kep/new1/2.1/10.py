import math

# Зчитування довжин катетів
a = float(input("Введіть довжину першого катета: "))
b = float(input("Введіть довжину другого катета: "))

# Обчислення гіпотенузи за теоремою Піфагора
c = math.sqrt(a**2 + b**2)

# Обчислення площі прямокутного трикутника
area = 0.5 * a * b

# Виведення результатів
print(f"Гіпотенуза = {c:.2f}")
print(f"Площа трикутника = {area:.2f}")
