f = open("io/data/file1")
print(f.readline())
print(f.readline(3))
print(f.readline(4))
print(f.readline(5))
print(f.readline())

with open('io/data/file1', 'ab') as f:
    try:
        f.readline()
    except OSError:
        print('OSError')
