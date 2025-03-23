# Швидкість світла (км/с)
speed_of_light = 299792

# Кількість секунд у годині та добі
seconds_per_hour = 60 * 60
seconds_per_day = seconds_per_hour * 24

# Обчислення відстані
distance_per_hour = speed_of_light * seconds_per_hour
distance_per_day = speed_of_light * seconds_per_day

# Вивід результатів
print(f"Відстань, яку світло долає за годину: {distance_per_hour} км")
print(f"Відстань, яку світло долає за добу: {distance_per_day} км")
