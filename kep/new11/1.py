cities = ["Київ", "Дніпро", "Івано-Франківськ", "Кременчук", "Харків", "Хмельницький", "Одеса", "Львів", "Запоріжжя", "Чернігів"]

with open("cities.txt", "w", encoding="utf-8") as f:
    for city in cities:
        f.write(city + "\n")

with open("cities.txt", "r", encoding="utf-8") as f:
    names = [line.strip() for line in f]

for name in names:
    if len(name) > 7:
        print(name)
