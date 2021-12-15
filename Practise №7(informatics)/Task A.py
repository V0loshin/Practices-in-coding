# Задача №113652
# A. Получить из 1 число N

"""
Задание:

Определить можно ли с использованием только операций «прибавить 3» 
и «прибавить 5» получить из числа 1 число N.

"""

def from_one_to_N(n):
    if n < 1: return("No")
    if n == 1:
        return("Yes") 
    if n > 0 and from_one_to_N(n-5) == "No":
        return from_one_to_N(n-3)
    else:
        return from_one_to_N(n-5)

# for i in range(200):
#    print(f"{i} - {from_one_to_N(i)}")