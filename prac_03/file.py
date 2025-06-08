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

# 2
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3
with



