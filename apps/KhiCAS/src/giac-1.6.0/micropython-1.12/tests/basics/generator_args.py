# Handling of "complicated" arg forms to generators
# https://github.com/micropython/micropython/issues/397
def gen(v=5):
    yield from range(v)

print(list(gen()))
print(list(gen(v=10)))


def g(*args, **kwargs):
    yield from args
    yield from kwargs.items()

print(list(g(1, 2, 3, foo="bar")))
