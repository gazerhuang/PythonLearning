class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)
        if item.area > self.free_area:
            print("%s 面积太大，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("BED", 4)
print(bed)
chest = HouseItem("CHEST", 2)
print(chest)
table = HouseItem("TABLE", 1.5)
print(table)

my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
my_home.add_item(HouseItem("Boom", 200))
print(my_home)