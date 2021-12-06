with open("io/data/file1", "rb") as f:
    print(f.seek(6))
    print(f.read(5))
    print(f.tell())

    print(f.seek(0, 1))
    print(f.read(4))
    print(f.tell())

    print(f.seek(-6, 2))
    print(f.read(20))
    print(f.tell())

    print(f.seek(0, 0))
    print(f.read(5))
    print(f.tell())

with open("io/data/file1", "rt") as f:
    print(f.seek(6))
    print(f.read(5))
    print(f.tell())
# seek closed file
f = open('io/data/file1', 'r')
f.close()
try:
    f.seek(1)
except (OSError, ValueError):
    # CPy raises ValueError, uPy raises OSError
    print('OSError or ValueError')
