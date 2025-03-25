import math

x = float(input("Введіть значення x: "))
y = (2*pow(x,2) - 1) / (pow(x,2) + math.sin(x)) - (2*x + 1) / ((x + 2) * (x + 3))
print(f"Результат y = {y:.2f}")