list_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
while True:
    if list_name[0] == 'Валера':
        print('Валера нашелся')
        break
    else:
        list_name.pop(0)