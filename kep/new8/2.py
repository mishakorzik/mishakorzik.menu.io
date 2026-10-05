words = tuple(input('Введіть слова через пропуск: ').split())

print('Введений кортеж:', words)

max_index = 0
for i in range(1, len(words)):
    if len(words[i]) > len(words[max_index]):
        max_index = i

print(f'Найдовше слово: {words[max_index]}')
print(f'Довжина: {len(words[max_index])}')
print(f'Індекс: {max_index}')
