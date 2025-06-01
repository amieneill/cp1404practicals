"""
CP1404 - Practical_01
Program 2: Sales Bonus
Name: Amie Neill
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Based on sales of ${sales:.2f}, your bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Goodbye")
