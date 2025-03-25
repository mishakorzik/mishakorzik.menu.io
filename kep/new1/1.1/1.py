import math

# Зчитування значення x з екрану
x = float(input("Введіть значення 'x': "))

# Перевірка, що x > 0
if x <= 0:
    print("Помилка: значення 'x' має бути додатним.")
else:
    # Обчислення значень виразів
    numerator = 2 * x**2 - math.sin(x)**2
    denominator = math.cos(2 * x) + x**2
    term1 = numerator / denominator
    term2 = (x + 1) / math.log(x)

    # Обчислення значення функції y
    y = term1 - term2
    print(f"Значення функції y = {y:.2f}")
