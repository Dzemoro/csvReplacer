import re

arr = []
with open(input("\033[92m == READ == \nEnter the file name (with extension): "), "r") as file:
    for x in file:
        y = x.replace(";","\";\"")
        y = y.replace("\n","\"\n")
        arr.append("\"" + y)
    file.close()

arr[0] = arr[0].replace("\"", "")
arr[len(arr)-1] = arr[len(arr)-1] + "\""

with open(input("\033[94m == WRITE NEW FILE == \nEnter the file name (with extension): "), "w") as file:
    for x in arr:
        file.write(x)
    file.close()

print("\n\033[1;31mThe file was saved successfully!")