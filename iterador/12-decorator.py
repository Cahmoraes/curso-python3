from m_decorator import uppercase_decorator, my_decorator


@my_decorator
@uppercase_decorator
def text():
    return "Hello World"


print(text())
