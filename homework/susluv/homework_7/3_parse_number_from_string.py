text1 = 'результат операции: 42'
text2 = 'результат операции: 54'
text3 = 'результат работы программы: 209'
text4 = 'результат: 2'


def get_number_from_text(text):
    return int(text.split(': ')[-1]) + 10


print(get_number_from_text(text1))
print(get_number_from_text(text2))
print(get_number_from_text(text3))
print(get_number_from_text(text4))
