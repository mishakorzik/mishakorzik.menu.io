# Введемо врожайність для кожного сорту пшениці
yield1 = float(input("Введіть врожайність першого сорту пшениці: "))
yield2 = float(input("Введіть врожайність другого сорту пшениці: "))
yield3 = float(input("Введіть врожайність третього сорту пшениці: "))

# Введемо площі кожного поля в
area1 = float(input("Введіть площу першого поля в (га): "))
area2 = float(input("Введіть площу другого поля в (га): "))
area3 = float(input("Введіть площу третього поля в (га): "))

#Обчислюємо врожай з кожного поля
harvest1 = yield1 * area1
harvest2 = yield2 * area2
harvest3 = yield2 * area3

# обчислюємо загальний врожай
total_harvest = harvest1 + harvest2 + harvest3

# вивід результатів
print("\n Результати: ")
print(f"З першого поля зібрали: {round(harvest1, 2)}")
print(f"З другого поля зібрали: {round(harvest2, 2)}")
print(f"З третього поля зібрали: {round(harvest3, 2)}")
print(f"Загальний врожай з трьох полів: {round(total_harvest, 2)}")