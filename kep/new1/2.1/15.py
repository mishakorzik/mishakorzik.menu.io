import math

# Зчитування координат вершин чотирикутника
x1, y1 = map(float, input("Введіть координати вершини A (x1 y1): ").split())
x2, y2 = map(float, input("Введіть координати вершини B (x2 y2): ").split())
x3, y3 = map(float, input("Введіть координати вершини C (x3 y3): ").split())
x4, y4 = map(float, input("Введіть координати вершини D (x4 y4): ").split())

# Обчислення довжин сторін
AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
CD = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
DA = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)

# Обчислення периметра
P = AB + BC + CD + DA

print(f"Периметр чотирикутника = {P:.2f}")
