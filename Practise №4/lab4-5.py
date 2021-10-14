import os

name = {}
surname = {}
patronymic = {}
birth_year = {}
illness = {}

for i in range(0,5):                                   # Завел цикл для того, чтобы консоль очищалась после введения данных об
    os.system('cls||clear')                            # очередном призывнике
    print("Введите данные о призывниках:\n")
    print("Призывник №", i+1, ":", sep="")
    surname[i] = input("Фамилия: ");                   # Последовательно записываю данные i-того призывника в отдельно выделенные
    name[i] = input("Имя: ");                          # словари
    patronymic[i] = input("Отчество: ");
    birth_year[i] = input("Год рождения: ");
    illness[i] = input("Заболевание: ");
     
os.system('cls||clear')                                # Очищаю экран для того чтобы вывести таблицу призывников 
print("Список призывников: \n")    

print("        Фамилия|"+"            Имя|"+"        Отчество|"+"  Год рождения|"+"    Заболевание\n")
for i in range(0,5):
    print("%15s|%15s|%16s|%14s|%15s" % (surname[i], name[i], patronymic[i], birth_year[i], illness[i]))