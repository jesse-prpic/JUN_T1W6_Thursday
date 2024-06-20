# print("Hello, welcome to programming with Python")

# a = 10
# b = 5
# result = a+b

# print(f"The result of adding {a} and {b} is {result}")

# print("Thank you")

# is_the_earth_flat = False
# print(is_the_earth_flat)

# x = 5
# y = 7
# z = 9

# print(x>y)

# Activity
# # Write a Python script that asks the user to input a numerical score and categorizes it into grades (A,B,C,D,E) based on the following criteria.
# 90- 100: A 
# 80-89: B
# 70-79: C
# 60-69: D
# 0 - 59: E

score = int(input("Enter the score (0-100):"))

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade for score {score} is {grade}")