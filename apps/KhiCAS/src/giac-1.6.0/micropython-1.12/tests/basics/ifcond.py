# test if conditions which are optimised by the compiler

print(6)

print(7)

print(8)

print(9)
print(12)

print(14)

print(17)

print('a')

print('b')

print('b')

print('a')

if (1,):
    print('a')

if not (1,):
    print('a')
else:
    print('b')

f2 = 0

def f(t1, t2, f1):
    print(1)
    if ():
        print(1)
    if (1,):
        print(1)
    if (1, 2):
        print(1)
    if t1 and t2:
        print(1)
    if (t1 and t2): # parsed differently to above
        print(1)
    if not (t1 and f1):
        print(1)
    if t1 or t2:
        print(1)
    if (t1 or t2): # parse differently to above
        print(1)
    if f1 or t1:
        print(1)
    if not (f1 or f2):
        print(1)
    if t1 and f1 or t1 and t2:
        print(1)
    if (f1 or t1) and (f2 or t2):
        print(1)

f(True, 1, False)
