"""
CP1404 - Practical_03
Files Program
Name: Amie Neill
"""

# 1
out_file = open("name.txt", 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()




