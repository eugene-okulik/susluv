def repeat_me1(func):
    def wrapper(*args, count=1, **kwargs):
        for i in range(1, count+1):
            func(*args, **kwargs)
    return wrapper


def repeat_me2(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(1, count+1):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_me1
def example1(text):
    print(text)


@repeat_me2(count=2)
def example2(text):
    print(text)


example1('print me1', count=2)
example2('print me2')
