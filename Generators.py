class Iterator:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current


x = Iterator(5)

for i in x:
    print(i)


def generator(n):
    for i in range(n):
        yield i

for i in generator(5):
    print(i)
print("break")

def gem():
    yield 1
    print("pause 1")
    yield 2
    print("pause 2")
    yield 3
    print("pause 3")
    yield 4

x =gem()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
