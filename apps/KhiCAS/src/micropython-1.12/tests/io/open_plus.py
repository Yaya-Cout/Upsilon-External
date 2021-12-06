try:
    import uos as os
except ImportError:
    import os

if not hasattr(os, "remove"):
    print("SKIP")
    raise SystemExit

# cleanup in case testfile exists
try:
    os.remove("testfile")
except OSError:
    pass

try:
    f = open("testfile", "r+b")
    print("Unexpectedly opened non-existing file")
except OSError:
    print("Expected OSError")
with open("testfile", "w+b") as f:
    f.write(b"1234567890")
    f.seek(0)
    print(f.read())
with open("testfile", "w+b") as f:
    f.write(b"abcdefg")
    f.seek(0)
    print(f.read())
with open("testfile", "r+b") as f:
    f.write(b"1234")
    f.seek(0)
    print(f.read())
# cleanup
try:
    os.remove("testfile")
except OSError:
    pass
