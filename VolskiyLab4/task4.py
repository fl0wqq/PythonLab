a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))


if a == b == c:
    print(f"Усі числа рівні між собою: {a}")


elif a == b and a > c:
    print(f"Числа a та b рівні і є найбільшими: {a}")
elif a == c and a > b:
    print(f"Числа a та c рівні і є найбільшими: {a}")
elif b == c and b > a:
    print(f"Числа b та c рівні і є найбільшими: {b}")


elif a >= b and a >= c:
    print(f"Найбільше число: a = {a}")
elif b >= a and b >= c:
    print(f"Найбільше число: b = {b}")
else:
    print(f"Найбільше число: c = {c}")