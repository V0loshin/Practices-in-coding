import calculator 

calc = calculator.Calculator()    # создаём новый экземпляр класса Calculator, определенный в модуле calculator 

calc.add(2)                       # увеличиваем значение calc на 2, используя функцию из класса Calculator
print(calc.get_current())         # выводим текущее значение calc на экран, используя функцию из того же класса



import my_module      # Импортировали модуль my_module 

my_module.hello_world("Илья")      # Вызовали функцию hello_world из модуля my_module

#----------------------------------------------------# 

import datetime 

current_date = datetime.date.today()      # из встроенного модуля datetime использовали функцию today() из класса date
print(current_date)       # Выводим текущую дату, используя встроенный модуль datetime 

#----------------------------------------------------#   

from calculator import Calculator 

calc = Calculator()     # теперь мы можем использовать класс Calculator без префикса calculator. 
calc.add(2) 
print(calc.get_current()) 

# Импортировал функцию hello_world из модуля my_module.   

from my_module import hello_world 
hello_world("Илья")  

# Результат тот же, что и при первом варианте вызова функции (с указанием имени модуля) 