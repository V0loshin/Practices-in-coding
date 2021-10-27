# Создание нового словаря 

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" и "Jerard" - ключи, соответствующие числa - значения 

print(phone_book) 

  
# Добавление нового элемента в словарь 

phone_book["Jill"] = 345 
print(phone_book) 
  

# Удаление пары “ключ-значение” из словаря 

del phone_book['John'] 
print(phone_book)

# Выведите номер Jane из телефонной книги 

print(phone_book['Jane'])           


phone_book = {"John": 123, "Jane": 234, "Jerard": 345, "Jill": 143}  # Создание нового словаря 
print(phone_book) 


# Добавление элемента с существющим ключом

phone_book["Jill"] = 456 
print(phone_book) 	# При добавлении элемента с существющим ключом, но другим значением, происходит замена 
                    # старого значения для ключа ["Jill"] на новое.
  

print(phone_book.keys())  # вывод всех ключей, которые есть в словаре



# Вывод всех номеров из телефонной книги: 

print(phone_book.values())           



grocery_list = ["fish", "tomato", 'apples']   	# Создание нового списка 

  

print("tomato" in grocery_list)    		# Проверка наличия элемента "tomato" в списке с помощью ключевого слова in 

  

grocery_dict = {"fish": 1, "tomato": 6, 'apples': 3}   # Создание нового словаря 

# Проверьте наличия в словаре записи с ключом "fish" и "potato" тем же способом, что и в списке: 

print("fish" in grocery_dict)
print("potato" in grocery_dict)          