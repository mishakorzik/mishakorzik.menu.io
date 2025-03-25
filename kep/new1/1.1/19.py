import math

x = float(input("Введіть x: "))
y = (pow(x,2)+1)/(pow(x,3)+3) + math.sin(x)/(2*x+3)
print(y)