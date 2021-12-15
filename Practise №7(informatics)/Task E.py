# Задача №113656
# E. Расставить скобки

"""
Задание:

Добавить открывающиеся и закрывающиеся скобки по следующему образцу:

"example" -> "(e(x(a(m)p)l)e)" - если количество букв нечётное
"card -> (c(ar)d)", но не "(c(a()r)d)" - если количество букв чётное

"""

def parentheses(string):

    if len(string) == 1 or len(string) == 2:
        return "(" + string + ")"
    else:
        new_string = string[1:len(string)-1]
        return "(" + string[0] + parentheses(new_string) + string[-1] + ")"     

print(parentheses("dcafg"))