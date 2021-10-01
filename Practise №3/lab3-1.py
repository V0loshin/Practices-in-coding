# Объединение двух строк с использованием символа `+` называется конкатенацией (concatenation).

# Python поддерживает умножение строк на числа.

hello = "Hello "

world = 'World'

# Получите строку "Hello World" с помощью конкатенации предыдущих переменных

print(hello+world)

# Получите строку "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello" с помощью операций со строками

hello = "Hello"
print(10*hello)

# Получите строку "Hello, World! World World Hello Hello!"  с помощью операций со строками
########

print(hello+", " + world + "! " + world, world, hello, hello + "!")

# Вы можете получить доступ к символу строки, если знаете его позицию.
# Например, str[index] даст символ в позиции index в строке str.

# Запомните! Строки всегда индексируются с 0.

python = "Python"

p_letter = python[0]  # Используйте переменную python для получения строки "pthn".
t_letter = python[2]
h_letter = python[3]
n_letter = python[5]
print(p_letter+t_letter+h_letter+n_letter)
########


# В Python индексы также могут быть отрицательными числами. Это позволяет начать отсчет с конца строки.
# Обратите внимание, что, поскольку -0 совпадает с 0, отрицательные индексы начинаются с -1.
# Таким образом, вы можете использовать отрицательные числа в операторе индексирования для подсчета символов с конца строки.

long_string = "This is a very long string!"

# Используйте отрицательный индекс для получения символа '!' из строки

symbol = long_string[-1]
print(symbol)