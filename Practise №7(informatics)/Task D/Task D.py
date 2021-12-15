# Задача №113655
# D. Вставить звёздочки

"""
Задание:

Добавить символ '*' (звездочка) между всеми буквами строки (кроме позиции перед первой 
буквой и после последней).

"""

def stars(string):
    new_string = string[:len(string)-1]

    if len(string) == 2:
        return string[0] + "*" + string[1]
    else:
        return(stars(new_string) + "*" + string[-1])

print(stars("LFsGthf"))
