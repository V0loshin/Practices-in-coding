import os
from module_6_5_2 import * 

current_dir = "C:\All\Coding practise\Practise №6\lab6-5.2"
file_name = ""
number = 0

for files in os.listdir(current_dir):
    if files == "input.txt": 
        file_name = files
        break

if file_name == "":
    print("Файл input.txt не найден в текущей директории!")
else:
    fin = open("C:\All\Coding practise\Practise №6\lab6-5.2\input.txt", "r")
    
    line = []
    line = fin.readline().split()
    number = int(line[0])

    fin.close()

if number != 0:
    fout = open("output.txt", "w")  

    fout.write(f"Число: {number}\n")
    fout.write(f"Количество цифр: {count_digits(number)}\n")
    fout.write(f"Сумма цифр: {sum_of_digits(number)}\n")
    fout.write(f"Произведение цифр: {multiplication_of_digits(number)}\n")

    fout.close()