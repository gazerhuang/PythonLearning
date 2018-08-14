class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("s")

    def test(self):
        print("fg %d" % self.__num2)
        self.__test()




class B(A):
    def demo(self):
        print("c %d" % self.num1)
        self.test()


b = B()
print(b)
b.demo()
