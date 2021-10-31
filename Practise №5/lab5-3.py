def hello_world():  		# Функция с именем "hello_world" 
    print("Hello, World!") 

# Определил функцию с именем fun, печатающую при своем вызове любой афоризм:

def aforizm():
    print("Афоризм — это литературное произведение, которое пишется для плагиаторов.")
    print("            - Антон Лигов")

# Это основная программа (Напишите эту заметку при написании основной программы) 

for i in range(3): 
    hello_world()   	# вызов функций, определенной выше  
    aforizm()

# заменил дубликаты строк в файле и реализовал подпрограмму, которая печатает сообщение на экран)  

def func():
    print('I want to be a function')

for i in range(3):  
    func()

#-----------------------------------------------------------------------------------------# 
 
def foo(x):                 # x - параметр функции 
    print("x = " + str(x)) 

foo(5)   	# Здесь мы вызываем функцию foo, передавая 5 в качестве аргумента. 

 
# Определяем функцию с именем square, печатающую квадрат передаваемого ей значения: 

def square(x):
    print(x**2)

square(4) 
square(8) 
square(15) 
square(23) 
square(42) 

#-----------------------------------------------------------------------------------------# 

def sum_two_numbers(a, b): 
    return a + b            # возвращаем результат    
 

c = sum_two_numbers(3, 12)  # присваиваем результат переменной 'c'   
print(c)


# Написана функция, возвращающая список из чисел Фибоначчи до n:

def fib(n): 
    result = [] 
    a = 1 
    b = 1 
    while a < n: 
        result.append(a) 
        tmp_var = b 
        b = a + b          # обновили значение переменной b, поместив в нее сумму значений 
        a = tmp_var        # обновили значение переменной a, поместив в нее значение вспомогательной переменной
    return result 

print(fib(10)) 