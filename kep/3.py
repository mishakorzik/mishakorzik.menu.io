# імпортуємо содуль
import math

#Функція для обчислення периметра і площі прямокутного трикутника
def triangle_properties(cathetus, angle):
    
    #Перетворення кута в радіани
    angle_rad = math.radians(angle)

    #Обчислення гіпотенузи за т. Піфагора
    hypotenuse = cathetus / math.sin(angle_rad)

    #Обчислення другого катету
    second_cathetus = cathetus * math.tan(angle_rad)

    # Обчислення периметра
    perimeter = cathetus + second_cathetus + hypotenuse

    # обчислення площі
    area = 0.5 * cathetus * second_cathetus
    return perimeter, area

#Введення катета і кута
cathetus = float(input("Введіть довжину катета: "))
angle = float(input("Введіть гострий кут (в градусах): "))

#Обчислення, виведення результатів
perimeter, area = triangle_properties(cathetus, angle)
print(f"Периметр трикутника: {perimeter:.2f}")
print(f"Площа трикутника: {area:.2f}")