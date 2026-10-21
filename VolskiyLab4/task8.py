balance = 5000

print("1 - Баланс | 2 - Внести | 3 - Зняти")
choice = input("Виберіть дію (1, 2 або 3): ")

if choice == "1":
    print(f"Ваш баланс: {balance} грн")
elif choice == "2":
    money = float(input("Скільки внести? "))
    if money > 0:
        print(f"Новий баланс: {balance + money} грн")
    else:
        print("Помилка суми!")
elif choice == "3":
    money = float(input("Скільки зняти? "))
    if 0 < money <= balance:
        print(f"Залишок: {balance - money} грн")
    else:
        print("Недостатньо коштів або помилка!")
else:
    print("Невірний вибір.")