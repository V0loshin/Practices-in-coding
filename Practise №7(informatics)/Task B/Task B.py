# Задача №113653 
# B. Наибольшая цифра

"""
Задание:

Выведите максимальную цифру, которая встречается во введенной строке,
содержащей только десятичные цифры.

"""

def biggest_digit(n):
    if n // 10 > 0 and biggest_digit(n // 10) > n % 10:
        return biggest_digit(n // 10)
    else:
        return n % 10   
            
print(biggest_digit(4342847))