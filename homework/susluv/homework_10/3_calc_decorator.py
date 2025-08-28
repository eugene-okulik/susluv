def decorated_calc(func):
    def wrapper(first, second, operation):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
        elif (first < 0) or (second < 0):  # unreachable?
            return func(first, second, '*')
        else:
            return func
    return wrapper


@decorated_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return None


print(calc(3, 3, '-'))  # 6 instead of 0
print(calc(4, 3, '+'))  # 1 instead of 7
print(calc(3, 4, '-'))  # 0.75 instead of -1
