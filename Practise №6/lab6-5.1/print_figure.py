def PrintRectangle(a, b, file_name):

    f = open(file_name, "w")
    
    for i in range(b):
        if i == 0 or i == b-1: 
            f.write(a * "*")
        else: 
            f.write("*"+(a-2)*" "+"*")
        f.write("\n")
    
    f.close()    

def PrintSquare(a, file_name):

    f = open(file_name, "w")
    
    for i in range(a):
        if i == 0 or i == a-1: 
            f.write(a * "*")
        else: 
            f.write("*"+(a-2)*" "+"*")
        f.write("\n")     
    
    f.close()       