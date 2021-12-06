import os
from module_6_5_3 import * 

file_name = ""  # создаём переменную для записи в неё имени необходимого файла

for files in os.listdir(os.getcwd() + "/Practise №6/lab6-5.3"):  # ищем файл input в текущей директории
    if files == "input.txt": 
        file_name = files
        break

f_out = open("Practise №6/lab6-5.3/output.txt", "w")

if file_name == "":  # если значение переменной не изменилось выводим соответствующее сообщение
    f_out.write("Файла input.txt нет в текущей директории.")
elif os.path.getsize(os.getcwd() + f"/Practise №6/lab6-5.3/{file_name}") != 0:  # если файл не пустой считываем содержимое

    f_in = open(os.getcwd() + f"/Practise №6/lab6-5.3/{file_name}", "r")
    N = int(f_in.readline())
    f_in.close()
    
    result = print_prime_numbers(N)  # получаем простые числа с помощью фукнции из модуля module_6_5_3
    for number in result:
        f_out.write(f"{number} ")
    
else:  # в ином случае выводим соответствующее сообщение
    f_out.write("Файл с входными данными не обнаружен.")

f_out.close()
