amount = float(input("Введіть суму покупки: "))

if amount <= 1000 and amount >= 0:
    discount = 0
elif amount > 1000 and amount <= 5000:
    discount = 10
elif amount > 5000 and amount <= 10000:
    discount = 20
elif amount > 10000:
    discount = 30
else:
    print("Сума не може бути від'ємною!")
    discount = None

if discount is not None:
    final_amount = amount * (1 - discount / 100)
    print(f"Сума покупки: {amount} грн")
    print(f"Знижка: {discount}%")
    print(f"Сума до сплати зі знижкою: {final_amount:.2f} грн")