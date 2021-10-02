import os

name = {}
surname = {}
patronymic = {}
birth_year = {}
illness = {}

for i in range(0,5):
    os.system('cls||clear')
    print("Введите данные о призывниках:\n")
    print("Призывник №", i+1, ":", sep="")
    surname[i] = input("Фамилия: ");
    name[i] = input("Имя: ");
    patronymic[i] = input("Отчество: ");
    birth_year[i] = input("Год рождения: ");
    illness[i] = input("Заболевание: ");
    os.system('cls||clear') 

print("Список призывников: \n")    

print("        Фамилия|"+"            Имя|"+"        Отчество|"+"  Год рождения|"+"    Заболевание\n")
for i in range(0,5):
    print("%15s|%15s|%16s|%14s|%15s" % (surname[i], name[i], patronymic[i], birth_year[i], illness[i]))