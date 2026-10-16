try:
    price = float(input("Введіть ціну товару: ").replace(",", "."))
    percent = float(input("Введіть відсоток знижки (від 0 до 100): ").replace(",", "."))

    if price < 0:
        raise ValueError("ціна товару не може бути від'ємною")

    if not 0 <= percent <= 100:
        raise ValueError("знижка повинна бути в межах від 0 до 100")

    discount = price * percent / 100
    final_price = price - discount
except ValueError as error:
    print("Помилка:", error)
except EOFError:
    print("Помилка: введення завершилося раніше, ніж потрібно (немає даних).")
else:
    print(f"Ціна без знижки: {price:.2f} грн")
    print(f"Знижка {percent:g}%:  {discount:.2f} грн")
    print(f"Ціна зі знижкою: {final_price:.2f} грн")
finally:
    print("Розрахунок завершено.")
