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

with open("testfile", "a") as f:
    f.write("foo")
with open("testfile") as f:
    print(f.read())
with open("testfile", "a") as f:
    f.write("bar")
with open("testfile") as f:
    print(f.read())
# cleanup
try:
    os.remove("testfile")
except OSError:
    pass
