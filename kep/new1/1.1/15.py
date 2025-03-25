import math

x = float(input("Введіть x: "))
y = (math.pow(x, 2) + 2*(x-1))/((x+1)*(x*math.sqrt(3))) + (2*math.sin(x)**2)/(2*x + 3**x)
print(f"Результат y = {y:.2f}")