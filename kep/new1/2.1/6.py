import math

# Зчитування координат точки 'M'
x0 = float(input("Введіть координату x точки M: "))
y0 = float(input("Введіть координату y точки M: "))
z0 = float(input("Введіть координату z точки M: "))

# Для першої площини: 22x - 4y - 20z - 45 = 0
a1, b1, c1, d1 = 22, -4, -20, -45
numerator1 = abs(a1 * x0 + b1 * y0 + c1 * z0 + d1)
denominator1 = math.sqrt(a1**2 + b1**2 + c1**2)
distance1 = numerator1 / denominator1

# Для другої площини: 3x - y + 5z + 1 = 0
a2, b2, c2, d2 = 3, -1, 5, 1
numerator2 = abs(a2 * x0 + b2 * y0 + c2 * z0 + d2)
denominator2 = math.sqrt(a2**2 + b2**2 + c2**2)
distance2 = numerator2 / denominator2

print(f"Відстань від точки M до площини 22x - 4y - 20z - 45 = 0, {distance1:.2f}")
print(f"Відстань від точки M до площини 3x - y + 5z + 1 = 0, {distance2:.2f}")
