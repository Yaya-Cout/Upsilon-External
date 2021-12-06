# Extended float comparisons

class Foo:
    pass

foo = Foo()

print(foo == 1.0)
print(1.0 == foo)
print(Foo == 1.0)
print([] == 1.0)
print({} == 1.0)

try:
    print(foo < 1.0)
except TypeError:
    print("TypeError")

try:
    print(foo > 1.0)
except TypeError:
    print("TypeError")
