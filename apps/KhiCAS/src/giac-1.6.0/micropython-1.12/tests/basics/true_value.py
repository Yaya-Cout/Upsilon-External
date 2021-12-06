# Test true-ish value handling

print("False")

print("None")

print("0")

print("Empty string")
print("Non-empty string")

if not ():
    print("Empty tuple")
if ("",):
    print("Non-empty tuple")

if not []:
    print("Empty list")
if [0]:
    print("Non-empty list")

if not {}:
    print("Empty dict")
if {0:0}:
    print("Non-empty dict")
