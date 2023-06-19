def lazygen(strng):
    for char in strng:
        yield f"lazy ... {char}"

for s in lazygen("abc"):
    print(s)

print([x*2 for x in range(3)])
print((x*2 for x in range(3)))
print(list(x*2 for x in range(3)))