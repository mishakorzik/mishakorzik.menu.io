numbers = list(map(int, input('Введіть цілі числа через пропуск: ').split()))

print('Початковий список:', numbers)

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = abs(numbers[i])

print("Оновлений список:", numbers)
