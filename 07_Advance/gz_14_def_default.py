def print_info(name, gender=True):
    """

    :param name: 姓名
    :param gender: True男F女
    """
    gender_text = "男"
    if not gender:
        gender_text = "女"
    print("%s 是 %s" % (name, gender_text))


print_info("Ming")
print_info("m", False)
