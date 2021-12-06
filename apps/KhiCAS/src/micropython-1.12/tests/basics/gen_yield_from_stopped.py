# Yielding from stopped generator is ok and results in None

def gen():
    return 1

f = gen()

def run():
    print((yield from f))
    print((yield from f))
    print((yield from f))

try:
    next(run())
except StopIteration:
    print("StopIteration")
