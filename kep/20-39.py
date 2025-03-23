import math

# Введення номера варіанта (i) та номера задачі (від 20 до 39)
i = float(input("Введіть номер варіанта (i): "))
task = int(input("Введіть номер задачі (20-39): "))

# Обчислення координат вершин трикутника
A = (0, 0)
B = (i, i - 1)
C = (-i, i + 1)

# Обчислення сторін трикутника
a = 2 * math.sqrt(i**2 + 1)
b = math.sqrt(2*i**2 + 2*i + 1)
c = math.sqrt(2*i**2 - 2*i + 1)

# Обчислення площі трикутника
Delta = i**2

# Напівпериметр
s = (a + b + c) / 2

# Висоти
h_a = 2 * Delta / a
h_b = 2 * Delta / b
h_c = 2 * Delta / c

# Медіани
m_a = 0.5 * math.sqrt(2*(b**2 + c**2) - a**2)
m_b = 0.5 * math.sqrt(2*(a**2 + c**2) - b**2)
m_c = 0.5 * math.sqrt(2*(a**2 + b**2) - c**2)

# Функція для обчислення бісектриси з вершини A, B, C
def bisector(side1, side2, opposite_side, vertex):
    cos_angle = (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)
    angle = math.acos(cos_angle)
    cos_half = math.sqrt((1 + cos_angle) / 2)
    # Бісектриса:
    w = 2 * side1 * side2 * cos_half / (side1 + side2)
    return w

w_a = bisector(b, c, a, 'A')
w_b = bisector(a, c, b, 'B')
w_c = bisector(a, b, c, 'C')

# Радіус вписаного кола
r_in = Delta / s

# Радіус описаного кола
R = (a * b * c) / (4 * Delta)

# Вибір задачі за номером:
if task == 20:
    # 20. Висота h_a та бісектриса w_c
    print(f"h_a = {h_a:.4f}")
    print(f"w_c = {w_c:.4f}")
elif task == 21:
    # 21. Медіана m_a та бісектриса w_b
    print(f"m_a = {m_a:.4f}")
    print(f"w_b = {w_b:.4f}")
elif task == 22:
    # 22. Бісектриса w_a та радіус вписаного кола r
    print(f"w_a = {w_a:.4f}")
    print(f"r (вписаного кола) = {r_in:.4f}")
elif task == 23:
    # 23. Висота h_a та медіана m_b
    print(f"h_a = {h_a:.4f}")
    print(f"m_b = {m_b:.4f}")
elif task == 24:
    #24. Медіана m_b та бісектриса w_c
    print(f"m_b = {m_b:.4f}")
    print(f"w_c = {w_c:.4f}")
elif task == 25:
    # 25. Бісектриса w_a та радіус описаного кола R
    print(f"w_a = {w_a:.4f}")
    print(f"R (описаного кола) = {R:.4f}")
elif task == 26:
    # 26. Висота h_b та бісектриса w_a
    print(f"h_b = {h_b:.4f}")
    print(f"w_a = {w_a:.4f}")
elif task == 27:
    # 27. Висота h_b та медіана m_c
    print(f"h_b = {h_b:.4f}")
    print(f"m_c = {m_c:.4f}")
elif task == 28:
    # 28. Висота h_a та радіус вписаного кола r
    print(f"h_a = {h_a:.4f}")
    print(f"r (вписаного кола) = {r_in:.4f}")
elif task == 29:
    # 29. Медіана m_c та бісектриса w_a
    print(f"m_c = {m_c:.4f}")
    print(f"w_a = {w_a:.4f}")
elif task == 30:
    # 30. Висота h_b та бісектриса w_c
    print(f"h_b = {h_b:.4f}")
    print(f"w_c = {w_c:.4f}")
elif task == 31:
    # 31. Медіана m_c та радіус вписаного кола r
    print(f"m_c = {m_c:.4f}")
    print(f"r (вписаного кола) = {r_in:.4f}")
elif task == 32:
    # 32. Висота h_a та медіана m_a
    print(f"h_a = {h_a:.4f}")
    print(f"m_a = {m_a:.4f}")
elif task == 33:
    # 33. Медіана m_a та радіус описаного кола R
    print(f"m_a = {m_a:.4f}")
    print(f"R (описаного кола) = {R:.4f}")
elif task == 34:
    # 34. Медіана m_a та бісектриса w_c
    print(f"m_a = {m_a:.4f}")
    print(f"w_c = {w_c:.4f}")
elif task == 35:
    #35. Медіана m_b та радіус вписаного кола r
    print(f"m_b = {m_b:.4f}")
    print(f"r (вписаного кола) = {r_in:.4f}")
elif task == 36:
    # 36. Висота h_c та медіана m_a
    print(f"h_c = {h_c:.4f}")
    print(f"m_a = {m_a:.4f}")
elif task == 37:
    # 37. Медіана m_c та радіус описаного кола R
    print(f"m_c = {m_c:.4f}")
    print(f"R (описаного кола) = {R:.4f}")
elif task == 38:
    # 38. Висота h_b та бісектриса w_b
    print(f"h_b = {h_b:.4f}")
    print(f"w_b = {w_b:.4f}")
elif task == 39:
    #39. Висота h_b та медіана m_b
    print(f"h_b = {h_b:.4f}")
    print(f"m_b = {m_b:.4f}")
else:
    print("Невідомий номер задачі. Введіть число від 20 до 39.")
