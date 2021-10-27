squares = [1, 4, 9, 16, 25]   	# Создание нового списка 

print(squares)      # Выводим на экран созданный список

print(squares[1:4])   # Вывожу на экран подсписок [4, 9, 16]    
 
print(squares[::-1])  # Вывожу все элементы списка в обратном порядке


animals = ['elephant', 'lion', 'tiger', "giraffe"]  # Создание нового списка 

print(animals) 

animals += ["monkey", 'dog']    	# Добавление новых элементов в список с помощью операции конкатенации

print(animals)          # Вывожу измененный список 
  
animals.append("dino")  		# Добавление нового элемента с помощью метода append() 

print(animals) 


animals[6] = "dinosaur"     # Заменил элемент 'dino' на 'dinosaur' 

print(animals)                

animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']   # Создание нового списка 
print(animals) 

animals[1:3] = ['cat']    	# Заменил сразу два элемента - 'lion' и 'tiger' - на один элемент - 'cat' 
print(animals) 

animals[1:3] = []     		# Удаление элементов 'cat' и 'giraffe' из списка 
print(animals) 

# Теперь полностью очистите список 

animals[:3] = []            # Полная очистка списка   
print(animals) 