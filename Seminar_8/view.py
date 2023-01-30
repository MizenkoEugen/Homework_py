def get_op():
    op = int(input(' 1 - добавить ученика \
    \n 2 - добавить предмет \
    \n 3 - добавить оценку \
    \n 4 - показать весь список \
    \n 5 - показать оценки ученика \
    \n 6 - выход \n'))
    return op


def input_student():
    name = input('Введите ФИО: ')
    return name


def input_less():
    less = input('Введите предмет: ')
    return less


def get_mark():
    name = input('Введите ФИО для оценки: ')
    less = input('Введите предмет для оценки: ')
    mark = input(f'Введите оценку {name} по {less}: ')
    return name, less, mark


def input_student_tab():
    name = input('Введите ФИО для просмотра оценок: ')
    return name
