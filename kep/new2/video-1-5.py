def task1():
    # Можнв зробити калькулятор в 1 строку але я вже переписав з відео
    print("Калькулятор:")
    print("Оберіть операцію: +, -, *, /")
    operation = input("Введіть операцію: ")
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if operation == '+':
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Помилка: ділення на нуль неможливе!")
        else:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Невірний вибір операції. Спробуйте ще раз!")

def task2():
    # Я імператор дискрімінанту
    a = float(input("Введіть коефіцієнт a: "))
    b = float(input("Введіть коефіцієнт b: "))
    c = float(input("Введіть коефіцієнт c: "))
    D = b**2 - 4 * a * c
  
    print(f"Дискрімінант: {D}")
    if D > 0:
        # Основне обчислення
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print(f"Рівняння має два корені: x1 = {x1} і x2 = {x2}")
    elif D == 0:
        # Основне обчислення
        x = -b / (2*a)
        print(f"Рівняння має один корінь: x = {x}")
    else:
        print("Рівняння не має дійсних коренів")

def task3():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    # Сума квадратів
    sum_of_squares = num1**2 + num2**2
    sum_of_numbers = num1 + num2
  
    if sum_of_squares > sum_of_numbers:
        print("Сума квадратів більша за суму чисел")
    elif sum_of_squares < sum_of_numbers:
        print("Сума чисел більша за суму квадратів")
    else:
        print("Сума квадратів дорівнює сумі чисел")

def task4():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    num3 = float(input("Введіть третє число: "))

    # Найбільше число
    if num1 >= num2 and num1 >= num3:
        maximum = num1
    elif num2 >= num1 and num2 >= num3:
        maximum = num2
    else:
        maximum = num3
    print(f"Найбільше число: {maximum}")

def task5():
    # Визначити знак зодіаку за місяцем
    month = int(input("Введіть місяць Вашого народження (1-12): "))
    day = int(input("Введіть день Вашого народження: "))
    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac = "Телець"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac = "Близнюки"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac = "Діва"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac = "Терези"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac = "Скорпіон"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac = "Стрілець"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac = "Козеріг"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac = "Водолій"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac = "Риби"
    else:
        zodiac = None

    # Результат
    if zodiac:
        print(f"Ваш знак зодіаку: {zodiac}")
    else:
        print("Невірно введена дата народження. Будь ласка, спробуйте ще раз.")

def task6():
    mark1 = int(input("Введіть оцінку за перший предмет: "))
    mark2 = int(input("Введіть оцінку за другий предмет: "))
    mark3 = int(input("Введіть оцінку за третій предмет: "))
    mark4 = int(input("Введіть оцінку за четвертий предмет: "))
    mark5 = int(input("Введіть оцінку за п'ятий предмет: "))

    # Обчислити середнє арифметичне
    average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

    if average >= 10:
        print("Відмінно!")
    elif 7 <= average <= 9:
        print("Добре!")
    elif 4 <= average <= 6:
        print("Задовільно!")
    else:
        print("Незадовільно!")

print("1. Калькулятор")
print("2. Розв’язання квадратного рівняння")
print("3. Порівняння суми квадратів і суми чисел")
print("4. Знаходження найбільшого з трьох чисел")
print("5. Визначення знаку зодіаку")
print("6. Обчислення середнього балу та оцінки")
    
choice = input("Ваш вибір (1-6): ")
    
if choice == '1':
    task1()
elif choice == '2':
    task2()
elif choice == '3':
    task3()
elif choice == '4':
    task4()
elif choice == '5':
    task5()
elif choice == '6':
    task6()
else:
    print("Невірний вибір! Спробуйте ще раз.")
