def task1():
    # Ввести 7 дійсних чисел та обчислити добуток елементів послідовності, значення яких є менше за 6.
    numbers = list(map(float, input("Введіть 7 чисел, розділених пробілом: ").split()))
    if len(numbers) != 7:
        print("Помилка: потрібно ввести рівно 7 чисел!")
        return
    prod = 1
    for num in numbers:
        if num < 6:
            prod *= num
    print("Добуток елементів (<6):", prod)

def task2():
    # Ввести 10 дійсних чисел та обчислити кількість додатних елементів.
    numbers = list(map(float, input("Введіть 10 чисел, розділених пробілом: ").split()))
    if len(numbers) != 10:
        print("Помилка: потрібно ввести рівно 10 чисел!")
        return
    count = sum(1 for num in numbers if num > 0)
    print("Кількість додатних елементів:", count)

def task3():
    # Ввести 6 дійсних чисел та обчислити суму відємних елементів.
    numbers = list(map(float, input("Введіть 6 чисел, розділених пробілом: ").split()))
    if len(numbers) != 6:
        print("Помилка: потрібно ввести рівно 6 чисел!")
        return
    s = sum(num for num in numbers if num < 0)
    print("Сума від'ємних елементів:", s)

def task4():
    # Ввести 5 дійсних чисел і визначити найменше та найбільше серед них.
    numbers = list(map(float, input("Введіть 5 чисел, розділених пробілом: ").split()))
    if len(numbers) != 5:
        print("Помилка: потрібно ввести рівно 5 чисел!")
        return
    mn, mx = min(numbers), max(numbers)
    print("Мінімум:", mn, "Максимум:", mx)

def task5():
    # Ввести 8 дійсних чисел та обчислити середнє арифметичне ненульових.
    numbers = list(map(float, input("Введіть 8 чисел, розділених пробілом: ").split()))
    if len(numbers) != 8:
        print("Помилка: потрібно ввести рівно 8 чисел!")
        return
    nonzero = [num for num in numbers if num != 0]
    if nonzero:
        avg = sum(nonzero) / len(nonzero)
        print("Середнє арифметичне ненульових:", avg)
    else:
        print("Немає ненульових елементів.")

def task6():
    # Ввести 9 дійсних чисел та обчислити суму елементів, абсолютне значення яких не перевищує 5.
    numbers = list(map(float, input("Введіть 9 чисел, розділених пробілом: ").split()))
    if len(numbers) != 9:
        print("Помилка: потрібно ввести рівно 9 чисел!")
        return
    s = sum(num for num in numbers if abs(num) <= 5)
    print("Сума елементів (|числа|<=5):", s)

def task7():
    # Ввести 11 дійсних чисел та обчислити кількість елементів, значення яких є більше за значення першого елемента.
    numbers = list(map(float, input("Введіть 11 чисел, розділених пробілом: ").split()))
    if len(numbers) != 11:
        print("Помилка: потрібно ввести рівно 11 чисел!")
        return
    first = numbers[0]
    count = sum(1 for num in numbers if num > first)
    print("Кількість елементів, більших за перший:", count)

def task8():
    # Ввести 6 дійсних чисел та обчислити добуток елементцв послідовності, значення яких перебувають у діапазоні [3, 6].
    numbers = list(map(float, input("Введіть 6 чисел, розділених пробілом: ").split()))
    if len(numbers) != 6:
        print("Помилка: потрібно ввести рівно 6 чисел!")
        return
    prod = 1
    found = False
    for num in numbers:
        if 3 <= num <= 6:
            prod *= num
            found = True
    if found:
        print("Добуток елементів у діапазоні [3,6]:", prod)
    else:
        print("Немає елементів у зазначеному діапазоні.")

def task9():
    # Ввести 8 дійсних чисел та обчислити середнє арифметичне додатних.
    numbers = list(map(float, input("Введіть 8 чисел, розділених пробілом: ").split()))
    if len(numbers) != 8:
        print("Помилка: потрібно ввести рівно 8 чисел!")
        return
    positives = [num for num in numbers if num > 0]
    if positives:
        avg = sum(positives) / len(positives)
        print("Середнє арифметичне додатних чисел:", avg)
    else:
        print("Немає додатних елементів.")

def task10():
    # Ввести 7 дійсних чисел та обчислити суму квадратів тих чисел, модуль яких не перевищує 3.
    numbers = list(map(float, input("Введіть 7 чисел, розділених пробілом: ").split()))
    if len(numbers) != 7:
        print("Помилка: потрібно ввести рівно 7 чисел!")
        return
    s = sum(num**2 for num in numbers if abs(num) <= 3)
    print("Сума квадратів чисел (|число|<=3):", s)

def task11():
    # Ввести 14 цілих чисел та обчислити кількість ненульових елементів.
    numbers = list(map(int, input("Введіть 14 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 14:
        print("Помилка: потрібно ввести рівно 14 чисел!")
        return
    count = sum(1 for num in numbers if num != 0)
    print("Кількість ненульових елементів:", count)

def task12():
    # Ввести 9 дійсних чисел та визначити мінімальний елемент послідовності.
    numbers = list(map(float, input("Введіть 9 чисел, розділених пробілом: ").split()))
    if len(numbers) != 9:
        print("Помилка: потрібно ввести рівно 9 чисел!")
        return
    print("Мінімальний елемент:", min(numbers))

def task13():
    # Ввести 6 цілих чисел та обчислити добуток ненульових елементів.
    numbers = list(map(int, input("Введіть 6 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 6:
        print("Помилка: потрібно ввести рівно 6 чисел!")
        return
    prod = 1
    found = False
    for num in numbers:
        if num != 0:
            prod *= num
            found = True
    if found:
        print("Добуток ненульових елементів:", prod)
    else:
        print("Немає ненульових елементів для множення.")

def task14():
    # Ввести 10 цілих чисел та обчислити середнє арифметичне елементів послідовності, значення яких перебувають у діапазоні [10, 20].
    numbers = list(map(int, input("Введіть 10 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 10:
        print("Помилка: потрібно ввести рівно 10 чисел!")
        return
    filtered = [num for num in numbers if 10 <= num <= 20]
    if filtered:
        avg = sum(filtered) / len(filtered)
        print("Середнє арифметичне чисел у діапазоні [10,20]:", avg)
    else:
        print("Немає елементів у заданому діапазоні.")

def task15():
    # Ввести 8 дійсних чисел та обчислити кількість елементів, значення яких перебувають у діапазоні [5, 10].
    numbers = list(map(float, input("Введіть 8 чисел, розділених пробілом: ").split()))
    if len(numbers) != 8:
        print("Помилка: потрібно ввести рівно 8 чисел!")
        return
    count = sum(1 for num in numbers if 5 <= num <= 10)
    print("Кількість елементів у діапазоні [5,10]:", count)

def task16():
    # Ввести 7 цілих чисел та визначити суму модулів усіх від'ємних елементів.
    numbers = list(map(int, input("Введіть 7 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 7:
        print("Помилка: потрібно ввести рівно 7 чисел!")
        return
    s = sum(abs(num) for num in numbers if num < 0)
    print("Сума модулів від'ємних елементів:", s)

def task17():
    # Ввести 9 дійсних чисел та обчислити добуток додатних елементів, значення яких не перевищує 4.
    numbers = list(map(float, input("Введіть 9 чисел, розділених пробілом: ").split()))
    if len(numbers) != 9:
        print("Помилка: потрібно ввести рівно 9 чисел!")
        return
    prod = 1
    found = False
    for num in numbers:
        if num > 0 and num <= 4:
            prod *= num
            found = True
    if found:
        print("Добуток додатних чисел (<=4):", prod)
    else:
        print("Немає додатних елементів, що не перевищують 4.")

def task18():
    # Ввести 12 дійсних чисел та обчислити кількість додатних і кількість від'ємних елементів послідовності.
    numbers = list(map(float, input("Введіть 12 чисел, розділених пробілом: ").split()))
    if len(numbers) != 12:
        print("Помилка: потрібно ввести рівно 12 чисел!")
        return
    pos = sum(1 for num in numbers if num > 0)
    neg = sum(1 for num in numbers if num < 0)
    print("Додатних елементів:", pos, "Від'ємних елементів:", neg)

def task19():
    # Ввести 8 цілих чисел та обчислити середнє арифметичне абсолютних значень усіх елементів послідовності.
    numbers = list(map(int, input("Введіть 8 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 8:
        print("Помилка: потрібно ввести рівно 8 чисел!")
        return
    avg = sum(abs(num) for num in numbers) / len(numbers)
    print("Середнє арифметичне абсолютних значень:", avg)

def task20():
    # Ввести 6 дійсних чисел та віднайти максимальний і мінімальний елементи та визначити, наскільки максимальний елемент є більшим за мінімальний.
    numbers = list(map(float, input("Введіть 6 чисел, розділених пробілом: ").split()))
    if len(numbers) != 6:
        print("Помилка: потрібно ввести рівно 6 чисел!")
        return
    mn = min(numbers)
    mx = max(numbers)
    diff = mx - mn
    print("Мінімальний:", mn, "Максимальний:", mx, "Різниця (макс - мін):", diff)

def task21():
    # Ввести 11 цілих чисел та обчислити суму тільки двоцифрових елементів.
    numbers = list(map(int, input("Введіть 11 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 11:
        print("Помилка: потрібно ввести рівно 11 чисел!")
        return
    s = sum(num for num in numbers if 10 <= abs(num) <= 99)
    print("Сума двоцифрових елементів:", s)

def task22():
    # Ввести 9 цілих чисел та обчислити добуток непарних елементів.
    numbers = list(map(int, input("Введіть 9 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 9:
        print("Помилка: потрібно ввести рівно 9 чисел!")
        return
    product = 1
    found = False
    for num in numbers:
        if num % 2 != 0:
            product *= num
            found = True
    if found:
        print("Добуток непарних елементів:", product)
    else:
        print("Немає непарних елементів.")

def task23():
    # Ввести 14 цілих чисел та обчислити кількість елементів, кратних до числа 3.
    numbers = list(map(int, input("Введіть 14 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 14:
        print("Помилка: потрібно ввести рівно 14 чисел!")
        return
    count = sum(1 for num in numbers if num % 3 == 0)
    print("Кількість елементів, кратних 3:", count)

def task24():
    # Ввести 7 цілих чисел та обчислити середнє арифметичне парних елементів.
    numbers = list(map(int, input("Введіть 7 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 7:
        print("Помилка: потрібно ввести рівно 7 чисел!")
        return
    evens = [num for num in numbers if num % 2 == 0]
    if evens:
        avg = sum(evens) / len(evens)
        print("Середнє арифметичне парних елементів:", avg)
    else:
        print("Немає парних елементів.")

def task25():
    # Ввести 6 дійсних чисел та обчислити суму елементів,
    numbers = list(map(float, input("Введіть 6 дійсних чисел, розділених пробілом: ").split()))
    if len(numbers) != 6:
        print("Помилка: потрібно ввести рівно 6 чисел!")
        return
    first = numbers[0]
    s = sum(num for num in numbers if num < first)
    print("Сума елементів, менших за перший елемент:", s)

def task26():
    # Ввести 9 цілих чисел та обчислити добуток одноцифрових елементів.
    numbers = list(map(int, input("Введіть 9 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 9:
        print("Помилка: потрібно ввести рівно 9 чисел!")
        return
    product = 1
    found = False
    for num in numbers:
        if abs(num) < 10:
            product *= num
            found = True
    if found:
        print("Добуток одноцифрових елементів:", product)
    else:
        print("Немає одноцифрових елементів.")

def task27():
    # Ввести 8 цілих чисел та визначити найменший з непарних додатних елементів цієї послідовності.
    numbers = list(map(int, input("Введіть 8 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 8:
        print("Помилка: потрібно ввести рівно 8 чисел!")
        return
    positives_odd = [num for num in numbers if num > 0 and num % 2 != 0]
    if positives_odd:
        print("Найменший непарний додатній елемент:", min(positives_odd))
    else:
        print("Немає непарних додатніх елементів.")

def task28():
    # Ввести 11 цілих чисел та обчислити середнє арифметичне елементів, кратних до числа 3.
    numbers = list(map(int, input("Введіть 11 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 11:
        print("Помилка: потрібно ввести рівно 11 чисел!")
        return
    div3 = [num for num in numbers if num % 3 == 0]
    if div3:
        avg = sum(div3) / len(div3)
        print("Середнє арифметичне елементів, кратних 3:", avg)
    else:
        print("Немає елементів, кратних 3.")

def task29():
    # Ввести 7 цілих чисел та обчислити добуток елементфв, кратних до числа 5.
    numbers = list(map(int, input("Введіть 7 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 7:
        print("Помилка: потрібно ввести рівно 7 чисел!")
        return
    product = 1
    found = False
    for num in numbers:
        if num % 5 == 0:
            product *= num
            found = True
    if found:
        print("Добуток елементів, кратних 5:", product)
    else:
        print("Немає елементів, кратних 5.")

def task30():
    # Ввести 10 цілих чисел та визначити найбільший з парних додатних елементів цієї послідовності.
    numbers = list(map(int, input("Введіть 10 цілих чисел, розділених пробілом: ").split()))
    if len(numbers) != 10:
        print("Помилка: потрібно ввести рівно 10 чисел!")
        return
    positive_evens = [num for num in numbers if num > 0 and num % 2 == 0]
    if positive_evens:
        print("Найбільший серед парних додатніх елементів:", max(positive_evens))
    else:
        print("Немає парних додатніх елементів.")

def main():
    tasks = {
        1: task1,
        2: task2,
        3: task3,
        4: task4,
        5: task5,
        6: task6,
        7: task7,
        8: task8,
        9: task9,
        10: task10,
        11: task11,
        12: task12,
        13: task13,
        14: task14,
        15: task15,
        16: task16,
        17: task17,
        18: task18,
        19: task19,
        20: task20,
        21: task21,
        22: task22,
        23: task23,
        24: task24,
        25: task25,
        26: task26,
        27: task27,
        28: task28,
        29: task29,
        30: task30
    }
    print("Оберіть номер задачі від 1 до 30:")
    choice = int(input("Ваш вибір: ").strip())
    if choice in tasks:
        tasks[choice]()
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()
