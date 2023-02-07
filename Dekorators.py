def my_decotrtor(func):
    def wrapper():
        print("noget sker inden funktions kaldet")
        func()
        print("noget sker efter funktions kaldet")
    return wrapper()

@my_decotrtor
def say_hello():
    print("hello")

