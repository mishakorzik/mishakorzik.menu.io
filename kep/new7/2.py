name = input("Назва пристрою: ")

if not name or name.startswith("-") or name.endswith("-"):
    print("Нє")
else:
    ok = True
    for ch in name:
        if not (ch.isascii() and (ch.isalnum() or ch == "-")):
            ok = False
    print("Так" if ok else "Ні")
