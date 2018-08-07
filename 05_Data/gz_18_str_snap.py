str = ["\t\n11","222  ","3333333  ","  44444"," 5"]

for a in str:
    print("|%s|" % a.strip().rjust(20," "))
