def print_prime_numbers(x):  # функция нахождения простых чисел решетом Эратосфена

    prime_numbers = []  # создаём список записи простых чисел
    prime_bool = [False, False]  # создаём первые два элемента (False для 0 и 1)

    for i in range(2, x+1):
        prime_bool.append(True)  # заполняем элементами "True" от 2 до введённого значения

    for p in range(2, x+1):
        if not(prime_bool[p]):
            continue
        else:
            prime_bool[p] = True
            i = 2
            while i*p <= x:
                prime_bool[i*p] = False  # задаем значение False для всех эл-тов кратных p (кроме p)
                i += 1

    for i in range(2, x+1):
        if prime_bool[i]:
            prime_numbers.append(i)  # записываем в список индексы элементов со значением True

    return prime_numbers
