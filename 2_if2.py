#Домашнее задание №1
#Условный оператор: Сравнение строк
#* Написать функцию, которая принимает на вход две строки
#* Проверить, является ли то, что передано функции, строками. 
#  Если нет - вернуть 0
#* Если строки одинаковые, вернуть 1
#* Если строки разные и первая длиннее, вернуть 2
#* Если строки разные и вторая строка 'learn', возвращает 3
#* Вызвать функцию несколько раз, передавая ей разные праметры 
#  и выводя на экран результаты



def length_line(line1, line2):
    #if not isinstance(line1, str) and isinstance(line2, str):
        #return '0'
    if len(line1) == len(line2):
        return 'ololo'
    elif len(line1) > len(line2):
        return '2'
    elif len(line1) > len(line2) and 'learn' in line2:
        return '3'
    else:
        length_line(line1, line2)

#line_1 = input('Введите первую строку - ')
#line_2 = input('Введите первую строку - ')

length_line(asdfh, asdf)