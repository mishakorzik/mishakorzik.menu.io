import math

# Введення значення 'x'
x = float(input("Введіть значення 'x': "))

if x == 0:
    print("Помилка: 'x' не може бути 0.")
elif math.cos(2*x) + x**2 == 0:
    print("Помилка: Ділення на нуль.")
else:
    ln_x2 = math.log(x**2)
    cos2 = math.cos(x)**2
    part1 = (ln_x2 + cos2) / (math.cos(2*x) + x**2)

    # Для коректного визначення кубічного кореня
    cube_root = math.copysign(abs(x)**(1/3), x)

    # Обчислення другої частини виразу
    part2 = cube_root / x

    y = part1 + part2
    print(f"Значення другого виразу = {y:.2f}")
