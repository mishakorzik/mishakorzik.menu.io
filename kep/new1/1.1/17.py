import math

x = float(input("Введіть значення x: "))
y = (3 * x - 2) / ((2 * x + 3) * (x + 1)) + math.sin(2 * x) / ((pow(x, 2) + 1) * (x + 2))
print(f"Результат y = {y:.2f}")