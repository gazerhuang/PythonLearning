# 全局变量
num = 10


def demo1():
    global num
    num = 1
    print("demo1: %d" % num)


def demo2():
    print("demo2: %d" % num)


demo1()
demo2()
