def get_answer(answer):
    while True:
        if answer == 'Пока':
            break
        else:
            answer = input('Как дела?')


user_answer = input('Как дела?')
get_answer(user_answer)