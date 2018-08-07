name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
print(name_list[0])
print(name_list.index("zhangsan"))

# 2.修改
name_list[1] = "李四"

# 3.增加
name_list.append("王小二")
name_list.insert(1, "2222")

temp_list = ["a", "b", "c"]
name_list.extend(temp_list)

# 4.删除
name_list.remove("2222")
name_list.pop()
name_list.pop(3)
# name_list.clear()

print(name_list)

