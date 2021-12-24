from random import randint
from sorts import *
import time
from prettytable import PrettyTable

"""
В данной программе:
b - обозначение сортировки методом пузырька (bubble_sort)
s - обозначение сортировки выбором (selection_sort)
q - обозначение быстрой сортировки (quick_sort)
"""


def sorting(some_list):  # функция возвращающая время сортировки тремя способами и сами отсортированные послед-сти
    start_time = time.time()
    b_sort = bubble_sort(some_list)  # сортируем последовательность методом пузырька
    time_b_sort = time.time() - start_time  # запоминаем время сортировки в соответствующую переменную

    start_time = time.time()
    s_sort = selection_sort(List)  # сортировка выбором
    time_s_sort = time.time() - start_time

    start_time = time.time()
    q_sort = quick_sort(List)  # Быстрая сортировка
    time_q_sort = time.time() - start_time

    return time_b_sort, time_s_sort, time_q_sort, b_sort, s_sort, q_sort


N = int(input("Введите количество элементов последовательности: "))

# Создаём список со случайными целыми числами:
List = []
for i in range(N):
    List.append(randint(0, 9))

print(Check(List))  # проверяю отсортирована ли последовательность до работы с ней


working_process = sorting(List)  # сортирую СЛУЧАЙНУЮ ПОСЛЕДОВАТЕЛЬНОСТЬ с помощью функции и записываю все результаты

print(check(working_process[3]))  # проверяю правильность результата сортировки для каждого метода
print(check(working_process[4]))
print(check(working_process[5]))

# записываю время выполнения сортировки случайной последовательности для каждого метода:
time_B_sort_random = working_process[0]
time_S_sort_random = working_process[1]
time_Q_sort_random = working_process[2]


working_process = sorting(working_process[3])  # сортирую УЖЕ ОСТОРТИРОВАННУЮ ПОСЛЕДОВАТЕЛЬНОСТЬ с помощью фукнции

print(check(working_process[3]))  # проверяю правильность результата сортировки для каждого метода
print(check(working_process[4]))
print(check(working_process[5]))

# записываю время выполнения сортировки уже отсортированной последовательности для каждого метода:
time_B_sorted = working_process[0]
time_S_sorted = working_process[1]
time_Q_sorted = working_process[2]


working_process = sorting(working_process[3][::-1])  # сортирую последовательность ОТСОРТИРОВАННУЮ В ОБР. ПОРЯДКЕ

print(check(working_process[3]))  # проверяю правильность результата сортировки для каждого метода
print(check(working_process[4]))
print(check(working_process[5]))

# записываю время выполнения сортировки уже отсортированной последовательности для каждого метода:
time_B_sorted_opp_way = working_process[0]
time_S_sorted_opp_way = working_process[1]
time_Q_sorted_opp_way = working_process[2]


# Формируем таблицу с результатами:

result_table = PrettyTable()
result_table.field_names = ["Методы", "Отсортированная", "Случайная", "Отс. в обратном порядке"]
result_table.add_row(["Метод пузырька", time_B_sorted, time_B_sort_random, time_B_sorted_opp_way])
result_table.add_row(["Сортировка выбором", time_S_sorted, time_S_sort_random, time_S_sorted_opp_way])
result_table.add_row(["Быстрая сортировка", time_Q_sorted, time_Q_sort_random, time_Q_sorted_opp_way])

# Выводим полученную таблицу в файл output.txt:

f_out = open("output.txt", "w")
f_out.write(f"N = {N}\n")
f_out.write(result_table.get_string(start=0, end=3))
f_out.close()
