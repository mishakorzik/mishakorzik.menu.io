import matplotlib.pyplot as plt

files = [120, 450, 75, 900, 33, 610, 250, 88]
names = ["Файл1", "Файл2", "Файл3", "Файл4", "Файл5", "Файл6", "Файл7", "Файл8"]

plt.bar(names, files)
plt.xlabel("Файл")
plt.ylabel("Розмір, МБ")
plt.title("Обсяг файлів")
plt.show()

big = max(files)
print("Найбільший файл:", names[files.index(big)], "-", big, "МБ")
