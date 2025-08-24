# python ругался, что не может вывести большое число, раскомментируй следующие строки, если ругается при запуске

# import sys

# sys.set_int_max_str_digits(100000)


def fibonacci():
    a = 0
    b = 1
    c = 0
    while True:
        yield a
        c = a
        a = b
        b = b + c


def get_number_from_fibonacci(n):
    count = 0
    for number in fibonacci():
        count += 1
        if count == n:
            return number


print(get_number_from_fibonacci(5))
print(get_number_from_fibonacci(200))
print(get_number_from_fibonacci(1000))
print(get_number_from_fibonacci(100000))
