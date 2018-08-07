students = [
    {"name": "TU"},
    {"name": "MEI"}
]

find = "TU1"

for stu_dict in students:
    print(stu_dict)

    if stu_dict["name"] == find:
        print("ok")
        break
else:
    print("no")


print("Over")
