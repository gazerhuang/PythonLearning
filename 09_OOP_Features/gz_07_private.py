class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("s")


class B(A):
    def demo(self):
        print("fs %s" % self.num1)

    def __test(self):
        pass


b = B()
print(b)
