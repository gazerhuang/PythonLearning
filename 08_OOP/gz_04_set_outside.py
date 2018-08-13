class Cat:

    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)


tom = Cat()

tom.eat()
tom.drink()
tom.name = "Tom"
