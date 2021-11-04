square = 1 

while square <= 10: 
    print(square)    # Эта операция выполнится 10 раз 
    square += 1      # Эта операция выполнится 10 раз  
print("Finished")    # Эта операция выполнится один раз 

print()  

square = 0 
number = 1 

# Вывожу квадраты чисел от 1 до 9 (1, 4, ... , 81), используя числовую переменную в цикле while. 

while number < 10:    
    square = number ** 2 
    print(square) 
    number += 1 
  

#-------------------------------------------------# 
print()

count = 0 
while True:  		# это условие всегда истинно 
    print(count) 
    count += 1 
    if count >= 5: 
        break           
# выходим из цикла, когда count >= 5, следовательно цикл выводит целые числа от 0 до 4, включая 4   

print()

# Выйдите из вечного цикла, правильно использовав break 

zoo = ["lion", 'tiger', 'elephant'] 
while True:             
    animal = zoo.pop()  # извлечь элемент с конца списка 
    print(animal) 
    if animal == 'elephant':
        break
# выходим из цикла, когда текущее животное - это 'elephant' 

 
#-----------------------------------------------# 
print()

for i in range(5): 
    if i == 3: 
        continue   	# пропустить остаток кода внутри цикла для заданного значения i 
    print(i) 
# данный цикл выведет числа: 0, 1, 2, 4. Число 3 будет пропущено

print()
 
# Выведем только нечетные числа 1, 3, 5, 7, 9:  

for x in range(10): 
    if x%2 == 0:    # Проверяем х на четность 
        continue   	# пропускаем print(x)  
    print(x) 