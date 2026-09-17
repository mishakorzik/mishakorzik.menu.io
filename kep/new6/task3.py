def f(n):
    if n == 0:
        return 1
    return f(n - 1) + (2 * n + 1)


n = int(input("Введіть n: "))

print("f(n) =", f(n))
