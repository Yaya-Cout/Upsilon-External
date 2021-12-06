# construct a bytes object from a generator
def gen():
    yield from range(4)
print(bytes(gen()))
