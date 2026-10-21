a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))

if a < b:
    print(f"Менше число: a = {a}")
elif b < a:
    print(f"Менше число: b = {b}")
else:
    print("Числа рівні між собою.")