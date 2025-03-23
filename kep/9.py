# Кількість секунд у хвилині
seconds_per_minute = 60

# Кількість хвилин у годині
minutes_per_hour = 60

# Кількість годин у добі
hours_per_day = 24

# Кількість днів у тижні та році
days_per_week = 7
days_per_year = 365

# Обчислення
seconds_per_day = seconds_per_minute * minutes_per_hour * hours_per_day
seconds_per_week = seconds_per_day * days_per_week
seconds_per_year = seconds_per_day * days_per_year

# Вивід результатів
print(f"Секунд у добі: {seconds_per_day}")
print(f"Секунд у тижні: {seconds_per_week}")
print(f"Секунд у році: {seconds_per_year}")
