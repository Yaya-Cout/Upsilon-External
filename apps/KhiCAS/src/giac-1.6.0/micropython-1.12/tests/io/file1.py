f = open("io/data/file1")
print(f.read(5))
print(f.readline())
print(f.read())
f = open("io/data/file1")
print(f.readlines())
f = open("io/data/file1","r")
print(f.readlines())
f = open("io/data/file1","rb")
print(f.readlines())
f = open("io/data/file1",mode="r")
print(f.readlines())
f = open("io/data/file1",mode="rb")
print(f.readlines())

with open('io/data/file1', 'r') as f:
    try:
        f.write('x')
    except OSError:
        print('OSError')
with open('io/data/file1', 'ab') as f:
    try:
        f.read(1)
    except OSError:
        print('OSError')
with open('io/data/file1', 'at') as f:
    try:
        f.read(1)
    except OSError:
        print('OSError')
with open('io/data/file1', 'ab') as f:
    try:
        f.read()
    except OSError:
        print('OSError')
