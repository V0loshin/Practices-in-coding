def bubble_sort(A):
    B = A
    N = len(B)
    R = N
    WasSwap = True
    while R > 1 and WasSwap:
        WasSwap = False
        for j in range(0, R-1):
            if B[j]>B[j+1]:
                B[j], B[j+1] = B[j+1], B[j]
                WasSwap = True
        R = R - 1
    return B    


def selection_sort(A):
    B = A
    N = len(B)
    for i in range(0,N-1):
        min = B[i]
        k = i
        for j in range(i+1,N):
            if B[j] < min:
                k = j
                min = B[j]
        B[k] = B[i]
        B[i] = min
    return B        


def quick_sort(A, L, R):
    B = A
    i = L 
    j = R
    Pivot = B[L]
    
    while i < j:
        while B[i] < Pivot: i += 1
        while Pivot < B[j]: j -= 1
        if i <= j:
            if B[i] > B[j]:
                B[i], B[j] = B[j], B[i]
            i += 1
            j -= 1
    
    if L < j:
        quick_sort(B, L, j)
    if i < R:
        quick_sort(B, i, R)

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
