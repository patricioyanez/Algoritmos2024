f = open("d.txt", "w")
f.write("holaaaaa")
f.close()

f = open("d.txt", "a")
f.write(" chauuuuuuu")
f.close()
#open and read the file after the overwriting:
f = open("d.txt", "r")
print(f.read())
