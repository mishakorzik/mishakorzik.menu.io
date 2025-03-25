import math

x = float(input("Введіть значення x: "))
y = (math.pow(x, 2) + 2 * pow.sin(x)) / ((2 * x + 1)) + (math.sqrt(x) - math.cos(x)) / ((2 * x + 1) * (math.log(math.pow(x, 2) + 1)))
print(f"Результат y = {y:.2f}")