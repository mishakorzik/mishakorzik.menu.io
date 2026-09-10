A = int(input("Введіть початок відрізка: "))
B = int(input("Введіть кінець відрізка: "))

numbers = []

for i in range(A, B + 1):
    if i % 2 == 0:
        numbers.append(i)

print(*numbers[::-1])
