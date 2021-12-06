# test while conditions which are optimised by the compiler

while 0:
    print(0)
print(1)

while 1:
    print(2)
    break

while 2:
    print(3)
    break

while -1:
    print(4)
    break

while False:
    print('a')
print('b')

while True:
    print('a')
    break

while not False:
    print('a')
    break

while not True:
    print('a')
print('b')
