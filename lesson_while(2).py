list_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name):
    while True:
        if list_name[0] == name:
            print(name, 'нашелся')
            break
        else:
            list_name.pop(0)

name1 = input()
find_person(name1)