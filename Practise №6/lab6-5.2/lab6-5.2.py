import os

def count_sum_mult_digits(x):  # функция вычисления количества цифер числа
    count = 0
    sum = 0
    mult = 1
    while x > 0:
        y = x % 10
        x = x // 10
        count += 1
        sum += y
        mult *= y
    return count, sum, mult 

current_dir = "C:/All/Coding practise/Practise №6/lab6-5.2"  # запоминаем путь к текущей директории
file_name = ""  # создаём переменную для записи в неё имени необходимого файла
number = 0

for files in os.listdir(os.getcwd() + "/Practise №6/lab6-5.2"):  # ищем файл input в текущей директории
    if files == "input.txt": 
        file_name = files
        break

if file_name == "":  # если значение переменной не изменилось выводим соответствующее сообщение
    print("Файл input.txt не найден в текущей директории!")
else:
    f_in = open("Practise №6/lab6-5.2/input.txt", "r")
    
    line = []
    line = f_in.readline().split()  # считываем данные из файла в список
    if len(line) != 0:
        number = int(line[0])  # берем из списка число

    f_in.close()

if len(line) != 0:
    
    f_out = open("Practise №6/lab6-5.2/output.txt", "w")

    f_out.write(f"Число: {number}\n")   # выводим все необходимые данные полученные с помощью фукнции count_sum_mult_digits
    f_out.write(f"Количество цифр: {count_sum_mult_digits(number)[0]}\n")
    f_out.write(f"Сумма цифр: {count_sum_mult_digits(number)[1]}\n")
    f_out.write(f"Произведение цифр: {count_sum_mult_digits(number)[2]}\n")

    f_out.close()
    