# Урожайність сортів
yield_per_hectare = [36, 40, 44]

# Площі полів (га) – потрібно задати користувачем
field_areas = [10, 12, 15]  # Приклад значень

# Обчислення врожаю для кожного поля
harvest_per_field = [yield_per_hectare[i] * field_areas[i] for i in range(len(yield_per_hectare))]

# Загальний врожай
total_harvest = sum(harvest_per_field)

# Вивід результатів
for i, harvest in enumerate(harvest_per_field):
    print(f"Поле {i+1}: {harvest} т")

print(f"Загальний врожай: {total_harvest} т")
