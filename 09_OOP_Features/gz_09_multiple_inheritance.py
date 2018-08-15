class A:
    def test(self):
        print("a")


class B:
    def demo(self):
        print("d")


class C(A, B):
    pass


c = C()
c.test()
c.demo()
