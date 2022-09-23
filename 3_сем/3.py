import zipfile
import os
file = zipfile.ZipFile("C:/Users/1/Desktop/Pyton/scripts1/3 lesson/main.zip")
file.extractall("C:/Users/1/Desktop/Pyton/scripts1/3 lesson")
a = []
for current_dir, dirs, files in os.walk("C:/Users/1/Desktop/Pyton/scripts1/3 lesson/main"): 
    for name in files:
        end = name[len(name) - 3] + name[len(name) - 2] + name[len(name) - 1]
        if end == ".py":
            a.append(current_dir)

print(*a, sep='\n')        