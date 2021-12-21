from random import randint
from sorts import *
import time
from prettytable import PrettyTable

N = int(input("Введите количество элементов последовательности: "))

# Создаём список со случайными целыми числами:
List = []
for i in range(N):
    List.append(randint(0, 9))

print(Check(List))  # проверяю отсортирован ли он

# Первый способ (сортировка методом пузырька):
start_time = time.time()
B_sort_random = bubble_sort(List)  # сортируем случайную последовательность
time_B_sort_random = time.time() - start_time  # запоминаем время сортировки в соответствующую переменную

start_time = time.time()
B_Sorted = bubble_sort(B_sort_random)
time_B_Sorted = time.time() - start_time

B_sort_opposite_way = B_sort_random[::-1]

start_time = time.time()
B_Sorted_opp_way = bubble_sort(B_sort_opposite_way)
time_B_Sorted_opp_way = time.time() - start_time

print(Check(B_sort_random))  # Проверяем отсортировалась ли последовательность


# Второй способ (сортировка выбором):
start_time = time.time()
S_sort_random = selection_sort(List)
time_S_sort_random = time.time() - start_time

start_time = time.time()
S_Sorted = selection_sort(B_sort_random)
time_S_Sorted = time.time() - start_time

S_sort_opposite_way = S_sort_random[::-1]

start_time = time.time()
S_Sorted_opp_way = selection_sort(S_sort_opposite_way)
time_S_Sorted_opp_way = time.time() - start_time

print(Check(S_Sorted))


# Третий способ (Быстрая сортировка):
start_time = time.time()
Q_sort_random = quick_sort(List, 0, len(List)-1)
time_Q_sort_random = time.time() - start_time

start_time = time.time()
Q_Sorted = quick_sort(Q_sort_random, 0, len(List)-1)
time_Q_Sorted = time.time() - start_time

Q_sort_opposite_way = Q_sort_random[::-1]

start_time = time.time()
Q_Sorted_opp_way = quick_sort(Q_sort_opposite_way, 0, len(List)-1)
time_Q_Sorted_opp_way = time.time() - start_time

print(Check(Q_sort_random))


# Формируем таблицу с результатами:

result_table = PrettyTable()
result_table.field_names = ["Методы", "Отсортированная", "Случайная", "Отс. в обратном порядке"]
result_table.add_row(["Метод пузырька", time_B_sort_random, time_B_Sorted, time_B_Sorted_opp_way])
result_table.add_row(["Метод пузырька", time_S_sort_random, time_S_Sorted, time_S_Sorted_opp_way])
result_table.add_row(["Метод пузырька", time_Q_sort_random, time_Q_Sorted, time_Q_Sorted_opp_way])

# Выводим полученную таблицу в файл output.txt:

f_out = open("output.txt", "w")
f_out.write(f"N = {N}\n")
f_out.write(result_table.get_string(start=0, end=3))
f_out.close()
