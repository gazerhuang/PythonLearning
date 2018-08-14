class Person:
    def __init__(self, new_name, new_weight):
        self.name = new_name
        self.weight = new_weight

    def __str__(self):
        return "%s 体重 %.2f kg" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


ming = Person("Ming", 75)
ming.run()
ming.run()
ming.run()
ming.eat()
print(ming)