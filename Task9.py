def is_triangle(angle1, angle2, angle3):
    return angle1 + angle2 + angle3 == 180

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))
if is_triangle(angle1, angle2, angle3):
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")
