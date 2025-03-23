#Імпорт бібліотеки
import math

#Введення старих цін та відсоткового зростання
old_price_1 = float(input("Введіть стару ціну першого товару: "))
old_price_2 = float(input("Введіть стару ціну другого товару: "))
percent = float(input("Введіть відсоток зростання ціни: "))

#Обчислення нових цін із використанням math.pow()
new_price_1 = old_price_1 * math.pow(1 + percent / 100, 1)
new_price_2 = old_price_2 * math.pow(1 + percent / 100, 1)

#Виведення старих та нових цін
print(f"Стара ціна першого товару: {old_price_1}; нова ціна першого товару: {new_price_1}")
print(f"Стара ціна другого товару: {old_price_2}; нова ціна другого товару: {new_price_2}")