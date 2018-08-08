def tes1t(num):
    print("在函数内部 %d 对应的内存地址 %d" % (num, id(num)))
    result = "hello"
    print("函数中返回地址： %d" % id(result))
    return result


a = 10
print("a地址：%d" % id(a))
r = tes1t(a)
print("%s 接收返回地址：%d" % (r, id(r)))
