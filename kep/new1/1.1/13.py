import math

x = float(input("Введіть значення x: "))
y = ((4*pow(x,2) - 2) * (x + 2)) / (2*x + 3) + (pow(x,2) * math.sin(x)) / (2*x + 1)
print(f"Результат y = {y:.2f}")