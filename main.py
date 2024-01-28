import math

def equal_3_triangle(side):
    return (math.sqrt(3) / 4) * side**2

def equal_2_triangle(base, height):
    return 0.5 * base * height

def right_triangle(cat1, cat2):
    return (cat1*cat2)/2

def common_triangle(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


ch = input("Enter triangle type: 1 - equal-side, 2 - 2-equal-side, 3 - right, 4 - common")

if ch == '1':
    side = int(input("Enter side length: "))
    print("Result, ", equal_3_triangle(side))
elif ch == '2':
    base = int(input("Enter base length: "))
    height = int(input("Enter height length: "))
    print("Result: ", equal_2_triangle(base, height))
elif ch == '3':
    cat1 = int(input("Enter cathetus 1: "))
    cat2 = int(input("Enter cathetus 2: "))
    print("Result: ", right_triangle(cat1, cat2))
elif ch == '4':
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 3: "))
    print("Result: ", common_triangle(side1, side2, side3))

    