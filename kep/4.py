# імпортуємо модуль
import math

# функція для обчислення довжини кола і площі круга
def circle_properties(diameter):
    #Обчислення радіусу
    radius = diameter / 2

    #Обчислення довжини кола
    circumference = 2 * math.pi * radius

    #Обчислення площі круга
    area = math.pi * pow(radius, 2)

    return circumference, area

# введення діаметра
diameter = float(input("Введіть діаметр круга: "))

# щбчислення та виведення результатів
circumference, area = circle_properties(diameter)
print(f"Довжина кола: {circumference:.2f}")
print(f"Площа круга: {area:.2f}")