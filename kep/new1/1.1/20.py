import math
x = float(input("Введіть x: "))
y = (4*pow(x,2)+3*x)/(3*x+4) + math.sin(x)/(2*math.cos(x)+1)
print(y)