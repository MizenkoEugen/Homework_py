from import_data import import_data
from export_data import export_data
from print_data import print_data
from print_name import print_name


def greeting():
    print("Телефонный справочник!")


def input_data():
    id = input("Введите ID контакта: ")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")

    return [id, first_name, last_name, phone_number, comment]


def choice_sep():
    sep = input("Введите разделитель ' ' или ',': ")
    if sep != " " and sep != ",":
        sep = choice_sep()
    return sep


def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - Импорт;\n\
    2 - Экспорт;\n\
    3 - Имя, Фамилия.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    elif ch == '3':
        data = export_data()
        print_name(data)
