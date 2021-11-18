import os
print(os.listdir())

def count_digits(x):
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count  

def sum_of_digits(x):
    sum = 0
    while x > 0:
        y = x % 10
        x = x // 10
        sum += y
    return sum   

def multiplication_of_digits(x):
    mult = 1
    while x > 0:
        y = x % 10
        x = x // 10
        mult *= y
    return mult           

current_dir = "C:\All\Coding practise\Practise №6\lab6-5.2"
file_name = ""
number = 0

if len(os.listdir(current_dir)) > 0:
    for files in os.listdir(current_dir):
        if files == "input.txt": 
            file_name = files
            break

if file_name == "":
    print("Файл input.txt не найден в текущей директории!")
else:
    f = open("C:\All\Coding practise\Practise №6\lab6-5.2\input.txt", "r")
    
    line = []
    line = f.readline().split()
    number = int(line[0])

    f.close()

print(number)
print(count_digits(number))
print(sum_of_digits(number))
print(multiplication_of_digits(number))

"""
for filenames in os.walk("."):
        for filename in filenames:
            print(filename)
"""            