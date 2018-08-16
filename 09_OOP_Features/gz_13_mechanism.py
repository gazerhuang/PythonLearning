class Tool:
    count = 0
    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("fuzi")
tool2 = Tool("lang")
tool3 = Tool("shui")
print(Tool.count)
print(tool1.count)
