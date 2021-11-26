from print_figure import print_rectangle
from print_figure import print_square

f_in = open("C:/All/Coding practise/Practise №6/lab6-5.1/input.txt", "r")

line1 = []

line1 = f_in.readline().split()  # считываем данные из первой строки файла input в список

a = int(line1[0])  # забираем из списка значение переменной а
if len(line1) == 2:  # если в списке два элемента, то забираем из списка значение переменной b
    b = int(line1[1])

file_name = f"C:/All/Coding practise/Practise №6/lab6-5.1/{f_in.readline()}"

f_in.close()

if len(line1) == 2:
    print_rectangle(a, b, file_name)  # если в списке два элемента, то выводим прямоугольник
else:
    print_square(a, file_name)  # иначе выводим квадрат
