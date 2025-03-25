import math

# Введення значення 'x'
x = float(input("Введіть значення 'x': "))

if x <= 0:
    print("Помилка: 'x' має бути додатнім для обчислення.")
elif 1 + x * math.cos(2 * x) == 0:
    print("Помилка: Ділення на нуль, оскільки 1 + x*cos(2x) = 0")
elif x * math.log(x) - 2 * (math.sin(x)**2) == 0:
    print("Помилка: Ділення на нуль, оскільки x*ln(x) - 2*sin²(x) = 0.")
else:
    # Обчислення першої частини
    numerator1 = 2 * (math.cos(x)**2)
    denominator1 = 1 + x * math.cos(2 * x)
    fraction1 = numerator1 / denominator1

    # Обчислення другої частини
    numerator2 = 0.3**x
    denominator2 = x * math.log(x) - 2 * (math.sin(x)**2)
    fraction2 = numerator2 / denominator2

    y = fraction1 + fraction2
    print(f"Значення другого виразу: {y:.2f}")
