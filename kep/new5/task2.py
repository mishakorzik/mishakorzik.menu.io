is_divisible_by_3 = lambda x: x % 3 == 0


number = int(input("Введіть число: "))

if is_divisible_by_3(number):
    print("Число ділиться на 3 без остачі")
else:
    print("Число не ділиться на 3 без остачі")
