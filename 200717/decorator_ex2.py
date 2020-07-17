def func():
    print("first function")

    def func1():
        print("first child function")

    def func2():
        print(" second child function")

    func1()
    func2()


func()
