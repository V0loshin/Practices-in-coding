def print_prime_numbers(x):

    prime_numbers = []
    prime_bool = [False, False]

    for i in range(2, x+1):
        prime_bool.append(True)

    for p in range(2, x+1):
        if prime_bool[p] == False:
            continue
        else:
            prime_bool[p] = True
            i = 2
            while i*p <= x:
                prime_bool[i*p] = False
                i += 1

    for i in range(2, x+1):
        if prime_bool[i] == True:
            prime_numbers.append(i)

    return prime_numbers      