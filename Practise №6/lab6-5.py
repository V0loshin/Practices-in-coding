from print_figure import PrintRectangle
from print_figure import PrintSquare

fin = open("input.txt", "r")

a = ""
b = ""
file = ""
flag = ""
 
for ch in fin.read():
    if ch == " ": 
        flag += " "
        continue
    if flag == "": a += f"{ch}"
    elif flag == " ": b += f"{ch}"
    else: file += f"{ch}"

fin.close()

if b == "": PrintSquare(a, file)
else: PrintRectangle(a, b, file)   

# PrintRectangle(3,4,"output.txt")
# PrintRectangle(2,6,"output.txt")
# PrintRectangle(2,2,"output.txt")
# PrintRectangle(6,3,"output.txt")

# PrintSquare(6,"output.txt")
