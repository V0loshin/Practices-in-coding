
a = set()  	# Создание пустого множества 



a.add(1)  	# Добавление элемента в множество 



a.add(2) 


a.add(1) 


print(a)  	# при добавлении в множество символов 1, 2, 1, в множестве хранятся символы 1 и 2, а вторая единица 
            # не записывается, так как множество хранит в себе только НЕ ПОВТОРЯЮЩИЕСЯ элементы.



b = set("hello")  # Преобразование строки в множество 


print(b)  	# При преобразовани строки в множество, строка разбивается на символы и множество хранит в себе
            # только неповторяющиеся символы строки в произвольном порядке. 



a = ["aa","ab","aa","ba"] 


print(set(a))       # Повторяющийся элемент списка "aa" удалится при выводе, так как список преобразовывается в множество


b = ['aa','ab','aa','ba'] 

print("aa" in b)        # True 

print(len(b) == 3)      # False


a = {1,2,3,4}   	# Создание множества 


b = {3,4,5,6}   


c = a.union(b) 		# Объединение множества 


print(c)  		


# Пересечение множеств a и b: 
 
d = a.intersection(b) 

print(d)