data = [
    "Київ;2967000;482",
    "Харків;1421000;1654",
    "Одеса;1010000;1794",
    "Дніпро;980000;1776",
    "Львів;717000;1256",
    "Івано-Франківськ;230000;1662",
    "Чернігів;285000;907",
]

with open("city_data.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

limit = int(input("Введіть населення: "))

cities = []
with open("city_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, population, year = line.strip().split(";")
        cities.append((name, int(population), int(year)))

for name, population, year in cities:
    if population > limit:
        print(name, population)

oldest = min(cities, key=lambda c: c[2])
print("Найстаріше місто:", oldest[0], oldest[2])
