has_ticket = True
knife_length = 30

if has_ticket:
    if knife_length > 20:
        print("warning %d" % knife_length)
    else:
        print("welcome")
else:
    print("go way")
