# функция вычисления количества целых точек:
def count_int_points(r, x, y):                
    count = 0   # завел счётчик

    x0 = x - r      # Определяю координаты(х0,у0) левого нижнего угла квадрата, в который вписана данная окружность,
    y0 = y - r      # а затем (ниже) правого верхнего угла(xn,yn), чтобы затем перебрать все целочисленные точки этого 
                    # квадрата и найти искомые
    xn = x + r
    yn = y + r

    for i in range(x0, xn+1):
        for j in range(y0, yn+1):
            if ((i-x)**2 + (j-y)**2)**0.5 <= r:   # Определяю расстояние от центра окружности до текущей точки и сравниваю с длиной радиуса.
                count += 1

    return count

import datetime
import time

start_time = time.time()        # запоминаю время начала работы программы

f_in = open("C:/All/Coding practise/Practise №6/lab6-5.4/input.txt", "r")

R = int(f_in.readline())     # считываю данные из первой строки в переменную R (радиус)
line2 = []
line2 = f_in.readline().split()      # считываю данные из второй строки в список откуда затем забираю в 
X = int(line2[0])                   # переменные Х и Y 
Y = int(line2[1])

f_in.close()

f_out = open("C:/All/Coding practise/Practise №6/lab6-5.4/output.txt", "w")

now = datetime.datetime.now()       # беру текущие дату и время и вывожу их
f_out.write(datetime.datetime.strftime(now, "%d.%m.%Y %H:%M \n"))

f_out.write(f"{count_int_points(R, X, Y)} \n")

f_out.write("%.8s" % (time.time() - start_time))     # получаю время работы программы 

f_out.close()
