import math
equation = input("Enter the equation: ")
equation = equation.replace(" ", "").lower()
equation_copy = equation
if "=0" in equation_copy or "=y" in equation_copy:
    equation_copy = equation_copy[:-2]
else:
    print("This is not a equation(format)!")
    exit()
if "x^2" in equation_copy:
    a = equation_copy.split("x^2")[0]
    equation_copy = equation_copy[len(a)+3:]
    if a == "": a = 1
    elif a == "-": a = -1
    a = float(a)
else:
    print("This is not a quadratic equation!")
    exit()
if "x" in equation_copy:
    b = equation_copy.split("x")[0]
    equation_copy = equation_copy[len(b)+1:]
    if b == "+": b = 1
    elif b == "-": b = -1
    b = float(b)
c = equation_copy if equation_copy else 0
c = float(c)
discriminant = b * b - 4 * a * c
if discriminant < 0:
    print("The equation: " + equation + " doesnt have a solution!")
elif discriminant == 0:
    result = -b/(2*a)
    print("The equation: " + equation + " has one solution x = " + str(result))
elif discriminant > 0:
    result1 = (-b+math.sqrt(discriminant))/(2*a)
    result2 = (-b-math.sqrt(discriminant))/(2*a)
    print("The equation: " + equation + " has two solutions x1 = " + str(result1) + "; x2 =" + str(result2))
