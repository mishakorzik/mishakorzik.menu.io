def task1(seq):
    # Підрахувати кількість елементів, які більші за попередній (дійсні числа).
    count = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i - 1]:
            count += 1
    return count

def task2(seq):
    # Обчислити суму елементів, що менші за перший (лійсні числа).
    if not seq:
        return 0
    first = seq[0]
    total = sum(x for x in seq if x < first)
    return total

def task3(seq):
    # Перевірити, чи послідовність упорядкована за спаданням (дійсні числа).
    return all(seq[i] >= seq[i+1] for i in range(len(seq)-1))

def task4(seq):
    # Обчислити min(a1+a2, a2+a3, ...) (натуральні числа).
    if len(seq) < 2:
        return None
    return min(seq[i] + seq[i+1] for i in range(len(seq) - 1))

def task5(seq):
    # Обчислити різницю між найменшим і першим числом (цілі числа).
    if not seq:
        return None
    return min(seq) - seq[0]

def task6(seq):
    # Обчислити min(a1, a3, a5, ...) + max(a2, a4, a6, ...) (дійсні числа).
    if not seq:
        return None
    odd_index_elements = seq[0::2]  # елементи з індексами 0,2,4,...
    even_index_elements = seq[1::2] # елементи з індексами 1,3,5,...
    if not even_index_elements:
        return min(odd_index_elements)
    return min(odd_index_elements) + max(even_index_elements)

def task7(seq):
    # Обчислити max(|a1-a2|, |a2-a3|, ...) (дійсні числа).
    if len(seq) < 2:
        return None
    return max(abs(seq[i] - seq[i+1]) for i in range(len(seq)-1))

def task8(seq):
    # Задача 8: Обчислити різницю між найбільшим і першим числом (цілі числа).
    if not seq:
        return None
    return max(seq) - seq[0]

def task9(seq):
    # Обчислити суму добутків сусідніх пар a1*a2 + a2*a3 + ... + a(n-1)*a(n) (дійсні числа).
    if len(seq) < 2:
        return 0
    return sum(seq[i] * seq[i+1] for i in range(len(seq)-1))

def task10(seq):
    # Обчислити добуток різниць сусідніх елементів (a2-a1)*(a3-a2)*...*(a(n)-a(n-1)) (дійсні числа).
    if len(seq) < 2:
        return None
    product = 1
    for i in range(len(seq)-1):
        product *= (seq[i+1] - seq[i])
    return product

def task11(seq):
    # Обчислити середнє арифметичне елементів, що менші за перший (дійсні числа).
    if not seq:
        return None
    filtered = [x for x in seq if x < seq[0]]
    if not filtered:
        return 0
    return sum(filtered) / len(filtered)

def task12(seq):
    # Перевірити, чи є в послідовності однакові сусідні числа (цілі числа).
    return any(seq[i] == seq[i+1] for i in range(len(seq)-1))

def task13(seq):
    # З'ясувати, чи складає послідовність зростаючу послідовність (цілі числа).
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def task14(seq):
    # Обчислити різницю між найбільшим і найменшим числом (цілі числа).
    if not seq:
        return None
    return max(seq) - min(seq)

def task15(seq):
    # Обчислити кількість і суму тих натуральних чисел, які діляться на 5 і не діляться на 7 (натуральні числа).
    count = 0
    total = 0
    for x in seq:
        if x % 5 == 0 and x % 7 != 0:
            count += 1
            total += x
    return count, total

def task16(seq):
    # Обчислити подвоєну суму всіх додатних членів послідовності (натуральні числа).
    return 2 * sum(seq)

def task17(seq):
    # Обчислити суму від'ємних елементів і кількість додатних елементів (дійсні числа).
    sum_negative = sum(x for x in seq if x < 0)
    count_positive = sum(1 for x in seq if x > 0)
    return sum_negative, count_positive

def task18(seq):
    # Знайти пару сусідніх елементів, між якими різниця (за модулем) мінімальна (дійсні числа).
    if len(seq) < 2:
        return None
    min_diff = abs(seq[1] - seq[0])
    pair = (seq[0], seq[1])
    for i in range(1, len(seq)-1):
        diff = abs(seq[i+1] - seq[i])
        if diff < min_diff:
            min_diff = diff
            pair = (seq[i], seq[i+1])
    return pair, min_diff

def task19(seq):
    # Обчислити відсотковий вміст від'ємних, нульових і додатних чисел (цілі числа).
    if not seq:
        return 0, 0, 0
    n = len(seq)
    neg = sum(1 for x in seq if x < 0)
    zero = sum(1 for x in seq if x == 0)
    pos = sum(1 for x in seq if x > 0)
    return (neg / n * 100, zero / n * 100, pos / n * 100)

def task20(seq):
    # Перевірити, чи є, крім першого, число, що дорівнює першому (цілі числа).
    if not seq:
        return False
    first = seq[0]
    return any(x == first for x in seq[1:])

def task21(seq):
    # Знайти перший нульовий елемент серед натуральних чисел (повертається індекс та значення).
    for i, x in enumerate(seq):
        if x == 0:
            return i, x
    return None

def task22(seq):
    # Обчислити кількість членів послідовності натуральних чисел, які мають парні порядкові номери (2-й, 4-й, ...) і є непарними числами.
    count = 0
    for i in range(1, len(seq), 2):
        if seq[i] % 2 != 0:
            count += 1
    return count

def task23(seq):
    # Обчислити суму квадратів тих елементів дійсних чисел, що менші за перший.
    if not seq:
        return 0
    first = seq[0]
    return sum(x**2 for x in seq if x < first)

def task24(seq):
    # Обчислити кількість трьохзначних чисел (натупальні числа).
    return sum(1 for x in seq if 100 <= x <= 999)

def task25(seq):
    # Обчислити суму елементів цілих чисел до першого від'ємного значення
    total = 0
    for x in seq:
        if x < 0:
            break
        total += x
    return total

def task26(seq):
    # Обчислити кількість елементів дійсних чисел, різниця яких із першим дорівнює 10 (|x - first| == 10).
    if not seq:
        return 0
    first = seq[0]
    return sum(1 for x in seq if abs(x - first) == 10)

def task27(seq):
    # Обчислити добуток елементів цілої послідовності до першого нульового значення.
    product = 1
    for x in seq:
        if x == 0:
            break
        product *= x
    return product

def task28(seq):
    # Обчислити суму залишків від ділення чисел на 2 (натуральні числа).
    return sum(x % 2 for x in seq)

def task29(seq):
    # Знайти останній від'ємний елемент дійсних чисел.
    last_negative = None
    for x in seq:
        if x < 0:
            last_negative = x
    return last_negative

def task30(seq):
    # Обчислти кількість двозначних чисел (натуральні числа).
    return sum(1 for x in seq if 10 <= x <= 99)

try:
    task_num = int(input("Введіть номер задачі (1-30): "))
except ValueError:
    print("Невірний ввід номеру задачі.")
    exit(1)

if task_num < 1 or task_num > 30:
    print("Номер задачі має бути від 1 до 30.")
    exit(1)

seq_str = input("Введіть послідовність чисел через пробіл: ")
try:
    seq = list(map(float, seq_str.split()))
except ValueError:
    print("Помилка перетворення введення в числа.")
    exit(1)

tasks = {
    1: task1,  2: task2,  3: task3,  4: task4,  5: task5,
    6: task6,  7: task7,  8: task8,  9: task9, 10: task10,
   11: task11, 12: task12, 13: task13, 14: task14, 15: task15,
   16: task16, 17: task17, 18: task18, 19: task19, 20: task20,
   21: task21, 22: task22, 23: task23, 24: task24, 25: task25,
   26: task26, 27: task27, 28: task28, 29: task29, 30: task30,
}

result = tasks[task_num](seq)
print("Результат задачі", task_num, ":", result)
