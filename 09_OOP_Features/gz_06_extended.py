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

    def bark(self):
        print("wa!!!")
        super().bark()
        #Dog.bark(self)
        print("#$@$#@")


xtq = Xiao()
xtq.bark()
