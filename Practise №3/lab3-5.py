name = input("Введите ваше имя >> ")
surname = input("Введите вашу фамилию >> ")
group = input("Ваша группа >> ")

print("\nПривет,", surname, name, "из группы", group+"!")

mail = input("Введи свою электронную почту: ")

print("\n"+surname.lower()[0:5]+2*name.lower()[0:5]+3*mail.lower()[0:5])