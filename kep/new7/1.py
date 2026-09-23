name = input("Назва пристрою: ")

if not name:
    print("Назва не може бути порожньою")
else:
    print(name.replace("-", "_").upper())
