def print_rectangle(a, b, file_name):

    f = open(file_name, "w")
    
    for i in range(b):
        if i == 0 or i == b-1:  # в первой и последней строке рисуем "a" звезд
            f.write(a * "*")
        else: 
            f.write("*"+(a-2)*" "+"*")  # в остальных рисуем по одной звезде в начале и конце строки
        f.write("\n")
    
    f.close()    


def print_square(a, file_name):

    f = open(file_name, "w")
    
    for i in range(a):
        if i == 0 or i == a-1: 
            f.write(a * "*")
        else: 
            f.write("*"+(a-2)*" "+"*")
        f.write("\n")     
    
    f.close()
