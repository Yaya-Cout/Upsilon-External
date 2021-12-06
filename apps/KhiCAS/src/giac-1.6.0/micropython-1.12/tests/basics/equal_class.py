# test equality for classes/instances to other types

class A:
    pass

class B:
    pass

class C(A):
    pass

print(A == None)
print(A is None)

print(A == A)
print(A() == A)
print(A() == A())

print(A == B)
print(A() == B)
print(A() == B())

print(A == C)
print(A() == C)
print(A() == C())
