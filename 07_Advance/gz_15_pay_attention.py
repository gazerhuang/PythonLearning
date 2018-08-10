def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 姓名
    :param gender: True男F女
    """
    gender_text = "男"
    if not gender:
        gender_text = "女"
    print("【%s】%s 是 %s" % (title, name, gender_text))


print_info("Ming", "a")
print_info("m", gender=False)
