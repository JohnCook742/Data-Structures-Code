print("Start")


def forloop():
    for i in range(0, 6, 1):
        print(i)


def recurse(start, stop, increment):
    # check if we need to stop
    if start >= stop:
        return
    # body of recursion
    print(start)
    # increment
    i = start + increment
    # recurse
    recurse(i, stop, increment)


def recursion():
    recurse(0, 6, 1)


forloop()
recursion()

print("End")
