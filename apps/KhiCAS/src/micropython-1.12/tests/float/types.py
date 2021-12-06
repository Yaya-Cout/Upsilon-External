# float types

print(float)
print(complex)

print(type(float()) == float)
print(type(complex()) == complex)

print(type(0.0) == float)
print(type(1j) == complex)

# hashing float types

d = {float: complex, complex: float}
print(len(d))
