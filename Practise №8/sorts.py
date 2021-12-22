def bubble_sort(A):  # сортировка методом пузырька
    B = A
    N = len(B)
    R = N
    WasSwap = True
    while R > 1 and WasSwap:  # перестанем заходить в цикл либо когда пройдём все элементы послед-сти, либо когда
                              # пройдёмся по части послед-сти с которой ещё не работали и при этом ничего в ней не поменяем
        WasSwap = False
        for j in range(0, R-1):
            if B[j]>B[j+1]:
                B[j], B[j+1] = B[j+1], B[j]
                WasSwap = True
        R = R - 1
    return B    


def selection_sort(A):  # сортировка выбором
    B = A
    N = len(B)
    for i in range(0,N-1):
        min = B[i]
        k = i
        for j in range(i+1,N):
            if B[j] < min:
                k = j
                min = B[j]
        B[k] = B[i]  # передаем переменной B[k] значение переменной B[i]
        B[i] = min   # а переменной B[i] передаем значение переменной B[k], таким образом меняя их местами
    return B        


def quick_sort(A):  # Быстрая сортировка
    B = A
    i = 0  # индекс первого символа последовательности
    j = len(B)-1  # индекс последнего символа последовательности
    L = i   # запоминаем индексы начала и конца последовательности в переменные L и R
    R = j
    Pivot = B[0]  # опорный элемент

    while i < j:
        while B[i] < Pivot:
            i += 1
        while Pivot < B[j]:
            j -= 1
        if i <= j:
            if B[i] > B[j]:
                B[i], B[j] = B[j], B[i]
            i += 1
            j -= 1
    
    if L < j:
        quick_sort(B[L:j+1])
    if i < R:
        quick_sort(B[i:R+1])

    return B    


def Check(A):
    Is_Sorted = True
    for i in range(len(A)-1):
        if A[i] <= A[i+1]:
            continue
        else:
            Is_Sorted = False
            break
    return Is_Sorted
