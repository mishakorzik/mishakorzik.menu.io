import math

# Зчитування значень змінних
x = float(input("Введіть значення x: "))
t = float(input("Введіть значення t: "))
g = float(input("Введіть значення g: "))

# Обчислення ш (гіперболічного синуса)
sh_x = (math.exp(x) - math.exp(-x)) / 2
sh_x_minus_1 = (math.exp(x - 1) - math.exp(-(x - 1))) / 2

# Обчислення функції W
W = sh_x * t * g * (x + 1) - t * (g ** 2) * (2 + sh_x_minus_1)

print(f"Значення функції W = {W:.2f}")
