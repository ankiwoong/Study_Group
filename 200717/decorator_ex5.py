def function1(function):
    def wrapper():
        print("hello")
        function()
        print("how are you?")

    return wrapper


@function1
def function2():
    print("pythonista")


function2()
