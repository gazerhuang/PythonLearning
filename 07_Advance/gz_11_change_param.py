def demo(num_list):
    print("inside")
    num_list.append(9)
    print(num_list)
    print("over")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
