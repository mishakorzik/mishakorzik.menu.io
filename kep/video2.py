# запитуємо у користувача початкову ціну товару
initial_price = float(input("Введіть початкову ціну товару: "))

# запитуємо розмір знижки
discount_percent = float(input("Введіть розмір знжки у %: "))

# обчислюємо суму знижки
discount_amount = (initial_price * discount_percent) / 100

#Обчислюємо фінальну ціну після знижки
final_price = initial_price - discount_amount

# Відповідь
print(f"Сума знижки: {round(discount_amount, 2)} грн")
print(f"Фінальна ціна після знижки {round(final_price, 2)} грн")