import math

#input variables
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

#distance formula
distance = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

#calculated distance between the two points
print(f"\n The distance between the two points is : {distance:.2f}")



"""
Using library is more practical because it helped simplifying my program instead of typing long formulas and made 
calculating easier by providing math.sqrt and math.pow. Without it, writing the program would be more difficult because 
i would have to rely on intuitive syntax.
"""
