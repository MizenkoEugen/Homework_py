# модуль экспорта данных 

def export_data():
    with open('phone.txt', 'r') as file:
        data = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ' ' in line:
                temp = line.strip().split(' ')
                data.append(temp)
    return data