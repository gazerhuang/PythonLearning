try:
    num = int(input("zheng:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("don't 0")
except ValueError:
    print("only num")
