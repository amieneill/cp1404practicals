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
with open("numbers.txt", 'r') as in_file:
    number_one = int(in_file.readline())
    number_two = int(in_file.readline())
print(number_one + number_two)




