import numpy
import random


def randomize_matrix(m, n):  # функция создания произвольной матрицы
    a = numpy.zeros((m, n))  # создаём нулевую матрицу
    for L in range(m):
        for J in range(n):
            a[L][J] += random.randint(0, 9)  # заполняем каждый её элемент произвольным числом от 0 до 9
    return a


f_in = open("C:/All/Coding practise/Practise №6/lab6-5.5/input.txt", "r")

line = []
line = f_in.readline().split()  # считываем данные из первой строки файла input в список

N = int(line[0])  # берем из списка два числа
M = int(line[1])

f_in.close()

A = randomize_matrix(N, M)  # создаем матрицу А
biggest_number = A.max()  # находим в ней наибольший элемент
K = random.randint(5, 15)  # генерируем число К из диапозона от 5 до 15
B = randomize_matrix(M, K)  # создаем матрицу В

f_out = open("C:/All/Coding practise/Practise №6/lab6-5.5/output.txt", "w")

f_out.write("Матрица А:\n")  # выводим в файл output матрицу А
for i in range(N):
    for j in range(M):
        f_out.write(f"{int(A[i][j])} ")
        A[i][j] = A[i][j] / biggest_number  # делим каждый элемент на наибольший
    f_out.write("\n")

f_out.write("Матрица B:\n")  # выводим в файл output матрицу В
for i in range(M):
    for j in range(K):
        f_out.write(f"{int(B[i][j])} ")
    f_out.write("\n")

C = A.dot(B)   # создаём матрицу С равную произведению матриц А и В (с помощью мтеода .dot)
f_out.write("Матрица A*B:\n")  # выводим в файл output матрицу C
for i in C:
    for j in i:
        f_out.write("{:>5s} ".format(str(round(j, 2))))   # выводим значения округленные до 2 знаков после запятой
    f_out.write("\n")                                     # и переведенные в тип str

f_out.close()
