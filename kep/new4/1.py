print("Ціна комплекту: 2700 грн")

q = int(input("Кількість комплектів: "))

if q < 10:
    discount = 0
    total = (2700 * q)
elif q >= 10 and q <= 19:
    discount = 10
    total = (2700 * q) * 0.9
elif q >= 20 and q <= 49:
    discount = 20
    total = (2700 * q) * 0.8
elif q >= 50 and q <= 99:
    discount = 30
    total = (2700 * q) * 0.7
elif q >= 100:
    discount = 40
    total = (2700 * q) * 0.6

print(f"Знижка: {discount}%")
print(f"Остаточна ціна: {total} грн")
