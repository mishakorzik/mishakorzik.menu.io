import math

# Обчислення виразу
x = float(input("Введіть значення x для першого виразу: "))

task1 = math.sin(x) + x**2
task2 = (1 + x**2) * (1 + 2*x)

if task1 == 0 or task2 == 0:
    print("Помилка: Ділення на нуль")
else:
    # Основні обчислення
    y = (3*x**2 + 2*x) / task1 - (2*x) / task2
    print(f"Значення першого виразу = {y:.2f}")
