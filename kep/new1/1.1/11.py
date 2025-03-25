import math

x = float(input("Введіть значення x: "))
y = (4*x**2 + 3*x) / ((1 + x) * (1 + 2*x)) + (2*x + 1) / (math.sin(x) + 1)
print(f"Результат y = {y:.2f}")