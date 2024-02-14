# decorator
def my_decorator(func):
    def wrap_func():
        print("attention to this sentence................")
        func()
        print("look at above text------------------")
    return wrap_func


@my_decorator
def helo():
    print("dsff")


helo()


@my_decorator
def bye():
    print("I will see you later")


bye()
