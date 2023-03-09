#!/usr/bin/python3
for c in range(10):
    for d in range(c + 1, 10):
        print("{}".format(str(c) + str(d)), end="")
        if int(str(c) + str(d)) < 89:
            print(", ", end="")
print("")
