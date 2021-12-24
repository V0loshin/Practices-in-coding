# a - список
def bubble_sort(a):  # сортировка методом пузырька
    b = a
    n = len(b)
    r = n
    was_swap = True
    while r > 1 and was_swap:  # перестанем заходить в цикл либо когда пройдём все элементы послед-сти, либо когда
                              # пройдёмся по части послед-сти с которой ещё не работали и при этом ничего в ней не поменяем
        was_swap = False
        for j in range(0, r-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                was_swap = True
        r = r - 1
    return b


def selection_sort(a):  # сортировка выбором
    b = a
    n = len(b)
    for i in range(0, n-1):
        min_number = b[i]
        k = i
        for j in range(i+1,n):
            if b[j] < min:
                k = j
                min_number = b[j]
        b[k] = b[i]  # передаем переменной B[k] значение переменной B[i]
        b[i] = min_number   # а переменной B[i] передаем значение переменной B[k], таким образом меняя их местами
    return b


def quick_sort(a):  # Быстрая сортировка
    b = a
    i = 0  # индекс первого символа последовательности
    j = len(b)-1  # индекс последнего символа последовательности
    l = i   # запоминаем индексы начала и конца последовательности в переменные L и R
    r = j
    pivot = B[0]  # опорный элемент

    while i < j:
        while b[i] < pivot:
            i += 1
        while pivot < b[j]:
            j -= 1
        if i <= j:
            if b[i] > b[j]:
                b[i], b[j] = b[j], b[i]
            i += 1
            j -= 1
    if l < j:
        quick_sort(b[l:j+1])
    if i < r:
        quick_sort(b[i:r+1])

    return b


def check(a):
    is_sorted = True
    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            continue
        else:
            is_sorted = False
            break
    return is_sorted
