stocks = [
    ("AA", 100, 9.22, -22.98),
    ("IBM", 50, 106.28, 15.18),
    ("CAT", 150, 35.46, -47.98),
    ("MSFT", 200, 20.89, -30.34),
    ("GE", 95, 13.48, -26.89),
    ("MSFT", 50, 20.89, -44.21),
    ("IBM", 100, 106.28, 35.84)
]


print(f"{'Name':<10} {'Shares':>10} {'Price':>10} {'Change':>10}")
print("-" * 43)


for name, shares, price, change in stocks:
    price_str = f"${price:.2f}"
    change_str = f"{change:.2f}%"
    print(f"{name:<10} {shares:>10} {price_str:>10} {change_str:>10}")