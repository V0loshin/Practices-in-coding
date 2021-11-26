import os
from module_6_5_2 import * 

current_dir = "C:/All/Coding practise/Practise №6/lab6-5.2"  # запоминаем путь к текущей директории
file_name = ""  # создаём переменную для записи в неё имени необходимого файла
number = 0

for files in os.listdir(current_dir):  # ищем файл input в текущей директории
    if files == "input.txt": 
        file_name = files
        break

if file_name == "":  # если значение переменной не изменилось выводим соответствующее сообщение
    print("Файл input.txt не найден в текущей директории!")
else:
    f_in = open("C:/All/Coding practise/Practise №6/lab6-5.2/input.txt", "r")
    
    line = []
    line = f_in.readline().split()  # считываем данные из файла в список
    number = int(line[0])  # берем из списка число

    f_in.close()

if number != 0:
    f_out = open("C:/All/Coding practise/Practise №6/lab6-5.2/output.txt", "w")

    f_out.write(f"Число: {number}\n")   # выводим все необходимые данные полученные с помощью фукнций из модуля module_6_5_2
    f_out.write(f"Количество цифр: {count_digits(number)}\n")
    f_out.write(f"Сумма цифр: {sum_of_digits(number)}\n")
    f_out.write(f"Произведение цифр: {multiplication_of_digits(number)}\n")

    f_out.close()