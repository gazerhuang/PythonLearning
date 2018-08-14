class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


bed = HouseItem("BED", 4)
print(bed)
chest = HouseItem("CHEST", 2)
print(chest)
table = HouseItem("TABLE", 1.5)
print(table)
