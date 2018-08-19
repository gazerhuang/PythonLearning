file = open("README")
file2 = open("README-COPY2", "w")

while True:

    text = file.readline()
    if not text:
        break
    file2.write(text)

file.close()
file2.close()