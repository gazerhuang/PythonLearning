class Cat:

    def eat(self):
        print("吃鱼")

    def drink(self):
        print("喝水")


tom = Cat()
tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

print(tom)
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
