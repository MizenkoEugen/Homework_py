# модуль импорта данных 

def import_data(data, sep):
    with open('phone.txt', 'a+') as file:
        file.write(sep.join(data))
        file.write(f"\n")