import math

x = float(input("Введіть значення x: "))
y = (pow(x, 2) - 2 * x) / ((2 * x + 3) * (x + 4)) + pow(x, 1/3) / (2 * x + 3)
print(f"Результат y = {y:.2f}")