day_number = int(input("Введіть номер дня тижня (від 1 до 7): "))

if day_number == 1:
    print("Понеділок")
elif day_number == 2:
    print("Вівторок")
elif day_number == 3:
    print("Середа")
elif day_number == 4:
    print("Четвер")
elif day_number == 5:
    print("П'ятниця")
elif day_number == 6:
    print("Субота")
elif day_number == 7:
    print("Неділя")
else:
    print("Помилка: введіть число від 1 до 7.")