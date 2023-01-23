def print_data(data):
    if len(data) > 0:
        print("ID".center(10), "Имя".center(20), "Фамилия".center(20),"№ телефона".center(15), "Комментарий".center(30))
        print("-"*100)
        for item in data:
            print(item[0].center(10), item[1].center(20), item[2].center(20), item[3].center(15), item[4].center(30))
    else:
        print("Справочник пуст!")

    