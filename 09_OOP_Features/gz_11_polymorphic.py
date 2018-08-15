class Dog:
    def __init__(self, name):
        self.name =name

    def game(self):
        print("play")


class XiaoTianDog(Dog):
    def game(self):
        print("play with Fly")


class Person(object):
    def __init__(self, name):
        self.name = name

    def game(self, dog):
        print("%s 和 %s play" % (self.name, dog.name))
        dog.game()


wangcai = XiaoTianDog("wangcai")
xiaoming = Person("xiaoming")
xiaoming.game(wangcai)
