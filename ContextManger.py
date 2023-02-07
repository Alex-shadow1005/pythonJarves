file = open("text.txt", "w")
try:
    file.write("hallo")
finally:
    file.close()

with open("file.txt", "w") as file:
    file.write("hello")


class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.file.close()
        return True

with File("file.txt", "w") as f:
    print("mid")
    f.write("hello lille mus")
    raise Exception


@context
def filex(filename, method):
    print("enter")
    filex = open(filename, method)
    yield filex
    filex.close()
    print("exit")

with filex("text.txt","w") as f:
    print("mid")
    f.write("hello lille mus")