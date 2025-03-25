import math
x = 1.52
c = 5
y = pow(abs(math.sqrt(x) + c), 1/3) * pow(math.sin(math.sqrt(x)), 2) + math.sqrt(x) * pow(math.cos(pow(abs(math.sqrt(x) + c), 1/3)), 2)
print(f"Результат y = {y:.2f}")