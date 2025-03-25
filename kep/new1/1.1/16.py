import math

x = float(input("Введіть значення x: "))
y = (4 * pow(x, 2) - pow(3, x)) / (2 * pow(x, 2) + 1) + math.log(x) / (2 * x + 3)
print(f"Результат y = {y:.2f}")