capitals = {
    "україна": "Київ",
    "польща": "Варшава",
    "німеччина": "Берлін",
    "франція": "Париж",
    "італія": "Рим",
    "іспанія": "Мадрид",
    "велика британія": "Лондон",
    "японія": "Токіо",
    "канада": "Оттава",
}

try:
    country = input("Введіть назву країни: ").strip().lower()

    if country == "":
        raise ValueError("назва країни не може бути порожньою")

    capital = capitals[country]
except ValueError as error:
    print("Помилка:", error)
except KeyError:
    print("Помилка: такої країни немає у словнику.")
    print("Доступні країни:", ", ".join(sorted(capitals)))
except EOFError:
    print("Помилка: введення завершилося раніше, ніж потрібно (немає даних).")
else:
    print(f"Столиця країни «{country.title()}» — {capital}.")
finally:
    print("Пошук у словнику завершено.")
