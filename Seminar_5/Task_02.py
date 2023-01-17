# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия для чисел:
# Входные данные: 111112222334445
# Выходные данные: 5142233415
# Также должно работать и для букв:
# Входные данные: AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:

# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def rle_encode(data_input):
    encoding = ''
    i = 0
    while i < len(data_input):
        count = 1
        while i + 1 < len(data_input) and data_input[i] == data_input[i+1]:
            count += 1
            i += 1
        encoding += str(count) + data_input[i]
        i += 1
    return encoding


def rle_decode(data_output):
    decoding = ''
    i = 0
    while i < len(data_output):
        count = 0
        while count < int(data_output[i]):
            count += 1
            decoding += data_output[i+1]
        i += 2
    return decoding


data = input("Введите данные для кодировки: ")
print(f"Зашифрованные данные: {rle_encode(data)}")
print(f"Дешифрованные данные: {rle_decode(rle_encode(data))}")
