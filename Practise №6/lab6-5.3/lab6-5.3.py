import os
from module_6_5_3 import * 

current_dir = "C:\All\Coding practise\Practise №6\lab6-5.3"
file_name = ""

for files in os.listdir(current_dir):
    if files == "input.txt": 
        file_name = files
        break

fout = open("output.txt", "w")

if file_name == "":
    fout.write("Файла input.txt нет в текущей директории.")
else:
    current_file = current_dir + "\\" + file_name

    if (os.path.getsize(current_file) != 0):

        fin = open(current_file, "r")
        N = int(fin.readline())
        fin.close()
    
        result = print_prime_numbers(N)
        for number in result:
            fout.write(f"{number} ")
    
    else: 
        fout.write("Файл с входными данными не обнаружен.")       

fout.close()
