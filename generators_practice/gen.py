# range is a generator
# generator is a subset of iterable

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


def gen(num):
    for i in range(num):
        yield i*2


for item in gen(1000):
    print(item)

#print(make_list(100))


def special_loop(iterable):
    # iter allows next() function
    iterator = iter(iterable)

    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break

special_loop([1,2,3])


class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if(MyGen.current < self.last):
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0,100)

for i in gen:
    print(i)