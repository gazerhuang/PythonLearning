# 名片列表
card_list = []


def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }

    card_list.append(card_dict)

    print(card_list)

    print("添加 %s 的名片成功" % name_str)


def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    if not card_list:
        print("没有名片记录，请添加")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    else:
        pass


def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    if not card_list:
        print("没有名片记录，请添加")
        return

    find_name = input("请输入要搜索的姓名：")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到 %s" % find_name)


def deal_card(find_dict):
    """处理名片

    :param find_dict: 名片
    """
    action_str = input("请输入对名片的操作："
                       "[1] 修改 [2] 删除 [0] 返回")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：【回车跳过】")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：【回车跳过】")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：【回车跳过】")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：【回车跳过】")
        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")


def input_card_info(dict_value, tip_message):
    """非空判断

    :param dict_value: 字典原值
    :param tip_message: 提示信息
    :return: 修改值/原值
    """
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
