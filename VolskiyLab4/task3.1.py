score = int(input("Введіть вашу оцінку (0-100): "))

if score >= 90 and score <= 100:
    print("Ваша оцінка А")
elif score >= 82 and score <= 89:
    print("Ваша оцінка B")
elif score >= 74 and score <= 81:
    print("Ваша оцінка C")
elif score >= 64 and score <= 73:
    print("Ваша оцінка D")
elif score >= 60 and score <= 63:
    print("Ваша оцінка E")
elif score >= 35 and score <= 39:
    print("Ваша оцінка FX")
elif score >= 0 and score <= 34:
    print("Ваша оцінка F")
else:
    print("Помилка: введено невірне значення бала (має бути від 0 до 100).")