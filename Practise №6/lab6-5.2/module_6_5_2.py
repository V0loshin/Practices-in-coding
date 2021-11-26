def count_digits(x):  # функция вычисления количества цифер числа
    count = 0
    while x > 0:
        x = x // 10
        count += 1
    return count  


def sum_of_digits(x):  # функция вычисления суммы всех цифр числа
    sum = 0
    while x > 0:
        y = x % 10
        x = x // 10
        sum += y
    return sum   


def multiplication_of_digits(x):  # функция вычисления произведения всех цифр числа
    mult = 1
    while x > 0:
        y = x % 10
        x = x // 10
        mult *= y
    return mult