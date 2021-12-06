from print_figure import print_rectangle
from print_figure import print_square
import os

f_in = open("Practise №6/lab6-5.1/input.txt", "r")

line1 = []

line1 = f_in.readline().split()  # считываем данные из первой строки файла input в список

a = int(line1[0])  # забираем из списка значение переменной а
if len(line1) == 2:  # если в списке два элемента, то забираем из списка значение переменной b
    b = int(line1[1])

line2 = f_in.readline()  # считываем данные из второй строки файла input в список
file_out_name = os.getcwd() + f"\\Practise №6\\lab6-5.1\\{line2}"

f_in.close()

if len(line1) == 2:
    print_rectangle(a, b, file_out_name)  # если в списке два элемента, то выводим прямоугольник
else:
    print_square(a, file_out_name)  # иначе выводим квадрат
