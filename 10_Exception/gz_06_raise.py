def input_password():
    pwd = input("password:")
    if len(pwd) >= 8:
        return pwd
    print("fq")
    ex = Exception("<8")
    raise ex


try:
    print(input_password())
except Exception as a:
    print(a)
