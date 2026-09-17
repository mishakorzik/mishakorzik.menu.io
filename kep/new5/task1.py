def sum_divisible(n, k):
    total = 0
    for i in range(1, n + 1):
        if i % k == 0:
            total = total + i
    return total


k = int(input("Введіть кратність k: "))

n1 = int(input("Введіть перше число n: "))
n2 = int(input("Введіть друге число n: "))
n3 = int(input("Введіть третє число n: "))

print("Сума 1:", sum_divisible(n1, k))
print("Сума 2:", sum_divisible(n2, k))
print("Сума 3:", sum_divisible(n3, k))
