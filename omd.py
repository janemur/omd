import random
#Добавила код, который рандомно выбирает одно из двух предложение и спрашивает поменять ли выбор

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    opt1 = 'Зонтик это хорошо. А вот про то, чтобы найти ей подходящую работу, речь уже не шла.'
    opt2 = 'Но вместо этого она взяла и покрасила стены:D Вам смешно, а у меня сейчас все это перед глазами происходит'

    choices = [opt1, opt2]
    print(random.choice(choices), "\n")
    change_mind()


def step2_no_umbrella():
    opt1 = 'Промокнуть? Нет! Насморк? Да! В общем, решила она взять такси!'
    opt2 = 'Тогда она взяла пистолет'

    choices = [opt1, opt2]
    print(random.choice(choices), "\n")
    change_mind()


def change_mind():
    print('Хотите поменять решение?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    return print('Кря 🦆')


if __name__ == '__main__':
    step1()
