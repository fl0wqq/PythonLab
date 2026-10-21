age = int(input("Введіть ваш вік: "))

if age < 18:
    print("Ви вважаєтеся Здоровим.")
else:
    has_diseases = input("Чи є у вас супутні захворювання? (так/ні): ").strip().lower()
    smokes = input("Чи палите ви? (так/ні): ").strip().lower()
    drinks = input("Чи вживаєте ви алкоголь? (так/ні): ").strip().lower()
    
    if has_diseases == "так" or smokes == "так" or drinks == "так":
        print("Ви вважаєтеся в зоні ризику.")
    else:
        print("Ви вважаєтеся Здоровим.")