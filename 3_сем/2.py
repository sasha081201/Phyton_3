def write_array(array, file_name):
    file_name.write('\n'.join(array))

a = ["something", "strang", "impossible", "very", "boring", "day"]
with open("file_test.txt", "w") as txt: 
    write_array(a, txt)
