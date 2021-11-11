from print_figure import PrintRectangle
from print_figure import PrintSquare

fin = open("C:/lab6-5.1/input.txt", "r")

line1 = []

line1 = fin.readline().split()

a = int(line1[0])
if len(line1) == 2:
    b = int(line1[1])

file_name = fin.readline()

fin.close()

if 'b' in globals(): PrintRectangle(a, b, file_name)
else: PrintSquare(a, file_name)

#if b == "": PrintSquare(a, file)
#else: PrintRectangle(a, b, file)   

# PrintRectangle(3,4,"output.txt")
# PrintRectangle(2,6,"output.txt")
# PrintRectangle(2,2,"output.txt")
# PrintRectangle(6,3,"output.txt")

# PrintSquare(6,"output.txt")
