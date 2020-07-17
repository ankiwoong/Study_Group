def function1(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print("it worked")

    return wrapper


@function1
def function2(name):
    print(f"{name}")


function2("python")
