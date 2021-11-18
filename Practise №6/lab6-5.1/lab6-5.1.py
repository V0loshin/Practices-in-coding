from print_figure import PrintRectangle
from print_figure import PrintSquare

fin = open("C:\All\Coding practise\Practise №6\lab6-5.1\input.txt", "r")

line1 = []

line1 = fin.readline().split()

a = int(line1[0])
if len(line1) == 2:
    b = int(line1[1])

file_name = fin.readline()

fin.close()

if 'b' in globals(): PrintRectangle(a, b, file_name)
else: PrintSquare(a, file_name)
