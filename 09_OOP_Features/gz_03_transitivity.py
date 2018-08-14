class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):

    def bark(self):
        print("bark")


class Xiao(Dog):
    def fly(self):
        print("fly")


xtq = Xiao()
xtq.fly()
xtq.drink()
