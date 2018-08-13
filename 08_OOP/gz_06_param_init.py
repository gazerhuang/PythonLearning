class Cat:

    def __init__(self, new_name):

        print("this is init")
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)


tom = Cat("Tom")
print(tom.name)

lazy_cat = Cat("Lazy")
lazy_cat.eat()
lazy_cat.drink()