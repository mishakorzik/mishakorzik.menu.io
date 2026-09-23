mac = input("MAC-адреса: ")
groups = mac.split(":")

ok = len(groups) == 6

for group in groups:
    if len(group) != 2:
        ok = False
    for ch in group:
        if ch not in "0123456789abcdefABCDEF":
            ok = False

if ok:
    print(mac.upper())
else:
    print("Помилка формату")
