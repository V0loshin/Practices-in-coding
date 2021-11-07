def PrintRectangle(a, b, file):
    name = file
    f = open(name, mode="w")
    
    for i in range(b):
        if i == 0 or i == b-1: f.write(a * "*")
        else: f.write("*"+(a-2)*" "+"*")
        f.write("\n")
    
    f.close()    

def PrintSquare(a, file):
    name = file
    f = open(name, mode="w")
    
    for i in range(a):
        if i == 0 or i == a-1: f.write(a * "*")
        else: f.write("*"+(a-2)*" "+"*")
        f.write("\n")     
    
    f.close()       