import os

conscripts = {} 

os.system('cls||clear')
number_of_conscr = int(input("Введите количество призывников: "))

for i in range(0,number_of_conscr):
    print(f"Данные о призывнике №{i+1}:\n")
    conscripts[f"surname{i+1}"] = input("Фамилия: ")
    conscripts[f"name{i+1}"] = input("Имя: ")
    conscripts[f"patr{i+1}"] = input("Отчество: ")
    conscripts[f"b_year{i+1}"] = input("Год рождения: ")
    conscripts[f"ill{i+1}"] = input("Заболевание: ")
    os.system('cls||clear')

print("Список призывников: \n")    

print("         Фамилия        |", end="")
print("          Имя          |", end="")
print("         Отчество          |", end="")
print("  Год рождения  |", end="")
print("             Заболевание\n")

for i in range(0,number_of_conscr):
    print("%24s" % conscripts[f"surname{i+1}"], end="")
    print("%24s" % conscripts[f"name{i+1}"], end="")
    print("%28s" % conscripts[f"patr{i+1}"], end="")
    print("%17s" % conscripts[f"b_year{i+1}"], end="")
    print("%34s\n" % conscripts[f"ill{i+1}"], end="")
    