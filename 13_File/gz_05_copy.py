file = open("README")
file2 = open("README-COPY", "w")

text =file.read()
file2.write(text)

file.close()
file2.close()
