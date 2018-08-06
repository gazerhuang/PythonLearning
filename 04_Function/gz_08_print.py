def print_line(char, time):
    """单行

    :param char: 字符
    :param time: 次数
    """
    print(char * time)


def print_time(char, time, num):
    """打印多行分隔线

    :param char: 字符
    :param time: 重复次数
    :param num: 行数
    """
    i = 0
    while i < num:
        print_line(char, time)
        i += 1


print_time("*", 100, 5)
