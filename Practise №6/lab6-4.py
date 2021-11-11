# Предварительно создал в папке с проектом файлы input.txt и input1.txt 

f = open("input.txt", "r")   # открываем файл "input.txt" для чтения

# Вывожу содержимое «input.txt» и первую строку «input1.txt». Затем закрываю файлы. 
for line in f.readlines():   # чтение построчно 
    print(line, end="")       
f.close()                    

print("\n")

f1 = open("input1.txt", "r")    # Начинаю работу с файлом "input1.txt" 

for line in f1.readlines():
    print(line)
    break  
f1.close()

#---------------------------------------------------------# 

zoo = ['lion', "elephant", 'monkey'] 

# Добавляю элементы списка zoo в файл "output.txt" :  

if __name__ == "__main__": 
    f = open("output.txt", "w")  # добавил нужный аргумент 

    for animal in zoo: 
        f.write(animal + '\n')  # добавил все элементы в файл

    f.close() # закрываю файл 