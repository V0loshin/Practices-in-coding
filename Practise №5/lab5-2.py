name = "John" 
age = 17 

if name == "John" or age == 17:  	# проверяем, зовут ли человека "John " или ему 17 лет  
# Если выполняется условие, то программа выводит следующие 2 строчки
    print("name is John") 		
    print("John is 17 years old") 


tasks = ['task1', 'task2']		# создаем список

tasks[:3] = []
if tasks == []:                 # Проверяем пустой ли список и выводим сообщение "List is empty", если он пустой 
    print("empty")  
   
  
x = 28 
if x < 0: 
    print('x < 0')	# выполняется только если x < 0 
elif x == 0: 
    print('x is zero')	# если x < 0 не истина, то проверяется равенство x == 0 
elif x == 1: 
    print('x == 1') 	# если x < 0 не истина и x == 0 не истина, проверяется равенство x == 1 
else: 
    print('non of the above is true')   # данный оператор будет выполняться если х!=0, х!=1 и x > 0 или другими словами -
                                        # только в том случае, если все вышеперечисленные проверки не оказались истинными
  
name = "John" 

# Проверяю имеет ли переменная name значение "John" 
 
if name == "John": 
    print(True) 
else: 
    print(False) 