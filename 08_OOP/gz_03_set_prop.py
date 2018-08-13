class Cat:

    def eat(self):
        print("%s 吃鱼" % self.name)

    def drink(self):
        print("%s 喝水" % self.name)


tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.name = "lazy"
lazy_cat.eat()
lazy_cat.drink()

print(tom)
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
