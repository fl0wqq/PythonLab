text_pass = "hhh lll hhh ddd sss"

pass_list = text_pass.split()

password = input("Введіть пароль: ")

if password in pass_list:
    print("Пароль правильний!")
    
else:
    print("Пароль неправильний!")
