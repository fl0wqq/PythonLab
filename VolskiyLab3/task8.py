title = input("Введіть назву книги: ")
author = input("Введіть автора (американського автора): ")
year = int(input("Введіть рік видання: "))
copies = int(input("Введіть кількість екземплярів: "))
price = float(input("Введіть вартість книги: "))
rating = float(input("Введіть рейтинг книги (0-10): "))


book_info = f"""
Інформація про книгу:
Назва: {title}
Автор: {author}
Рік видання: {year}
Кількість екземплярів: {copies:,}
Вартість: ${price:.2f}
Рейтинг: {rating:.2f}
"""

print(book_info)