import math

# Функция определяющая вид треугольника по длинам его сторон:
# a,b,c - длины сторон треугольника

def triangle(a,b,c):
    while (True):
        if a == 0 or b == 0 or c == 0:                    # Проверяем существует ли треугольник (если все стороны нулевые или
            print("Треугольник не существует!")           # сумма каких-то двух сторон оказалась меньше или равной третей стороне, то
            break                                         # то такой треугольник не существует)
        if (a + b <= c or c + b <= a or a + c <= b): 
            print("Треугольник не существует!")
            break 
        elif a == b and b == c: 
            print("Треугольник равносторонний!")
            break
        elif a == b or b == c or a == c: 
            print("Треугольник равнобедренный!")
            break
        else:                                             # Если результатом всех проверок выше не была истина, то функция возвращает
            print("Треугольник общего вида")              # данный результат
            break


triangle(-1, 2, 4)      # Набор тестов для функции triangle
triangle(0, 0, 0)    
triangle(2, 1, 1)    
triangle(1, 1, 1)    
triangle(2, 2, 1)    
triangle(3, 4, 5)    
triangle(6, 7, 8)   


# Функция высчитывающая корни квадратного уравнения и их количество 
# a,b,с - коэфициенты квадратного уравнения

def square_equation(a,b,c):
    print("Уравнение (%.5f)*x^2 + (%.5f)*x + (%.5f) = 0 \n" % (a,b,c))
    while (True): 
        if a == 0 and b == 0: 
            print("При таких коэфициентах квадратное уравнение не имеет смысла!")      # Проверяем значение корней a и b перед тем, 
            break                                                                      # как считать дискриминант
        elif a == 0: 
            print("Количество корней: 1")
            x1 = -1*(c/b)     
            print("%.5f" % x1)
            break
        
        Discr = b**2 - 4*a*c        # Высчитываем дискриминант и в зависимости от результата считаем корни 

        if Discr > 0:
            print("Количество корней: 2") 
            x1 = (-1*b + math.sqrt(Discr))/2*a
            x2 = (-1*b - math.sqrt(Discr))/2*a
            print("%.5f" % (x1))
            print("%.5f" % (x2))
            break
        elif Discr == 0:
            print("Количество корней: 1") 
            x1 = (-1*b)/(2*a)
            print("%.5f" % x1) 
            print("%.5f" % x1)
            break 
        elif Discr < 0: 
            print("Количество корней: 0")          
            break
    print()    

square_equation(1, -7, 12)       # Набор тестов для функции square_equation
square_equation(1, 4, 4)
square_equation(4, 0, -16)
square_equation(1, 4, 5)

# Функция вычисления времени прибытия поезда и количества полных суток прошедших за время пути  
# h_dep - часы отправления
# m_dep - минуты отправления
# h_time - часов в пути
# m_time - минут в пути

def arriving_time(h_dep, m_dep, h_time, m_time):
    
    number_of_days = (h_time*60 + m_time) // 60 // 24      # Мои комментарии для данных вычислений находятся в файле 
                                                           # "Комментарии к файлу lab5-4"
    
    h_arr = (h_dep*60 + m_dep + h_time*60 + m_time) // 60 % 24      # h_arr - час прибытия
    m_arr = (h_dep*60 + m_dep + h_time*60 + m_time) % 60            # m_arr - минуты прибытия
    
    print("%02d hours : %02d minutes" % (h_arr, m_arr))
    print(f"{number_of_days} days \n")


arriving_time(12, 20, 20, 40)       # Набор тестов для функции arriving_time
arriving_time(1, 15, 36, 37)
arriving_time(0, 48, 48, 15)


def price(summa):

    rub = summa // 100      # Узнали количество рублей и копеек для данной покупки
    kop = summa % 100

    # В файле "Комментарии к файлу lab5-4" приведены некоторые мои комментарии относительно определения
    # падежа у слов Рубль и Копейка

    if rub != 0:
        if (rub % 100 > 10) and (rub % 100 < 15): print(f"{rub} РУБЛЕЙ")
        elif (rub % 10 == 1): print(f"{rub} РУБЛЬ")
        elif (rub % 10 > 1) and (rub % 10 < 5): print(f"{rub} РУБЛЯ")
        elif (rub % 10 > 4)  or (rub % 10 == 0): print(f"{rub} РУБЛЕЙ")

    if kop != 0:
        if (kop % 100 > 10) and (kop % 100 < 15): print(f"{kop} КОПЕЕК")
        elif (kop % 10 == 1): print(f"{kop} КОПЕЙКА")
        elif (kop % 10 > 1) and (kop % 10 < 5): print(f"{kop} КОПЕЙКИ")
        elif (kop % 10 > 4)  or (kop % 10 == 0): print(f"{kop} КОПЕЕК")   

    print()     

price(101)          # Набор тестов для функции price
price(13)
price(99999)
price(100000)