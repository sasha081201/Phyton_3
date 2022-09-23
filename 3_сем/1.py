
with open("lines.txt", "w+") as txt: 
    for i in range(18):
        txt.write("    I'm a string of text   \n")
with open("lines.txt", "r+") as file:
    for line in file:
        print(line.strip())
file.close()