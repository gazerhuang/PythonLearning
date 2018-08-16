def demo1():
    return int(input(":"))


def demo2():
    demo1()

try:
    print(demo2())
except Exception as result:
    print(result)
