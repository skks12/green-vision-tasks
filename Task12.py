import math

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def milk_cost(volume):
    return volume * 40

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume = cylinder_volume(radius, height)
cost = milk_cost(volume / 1000)  # converting volume to liters
print(f"The volume of the cylinder is: {volume:.2f} cubic units")
print(f"The cost of milk to fill the cylinder is: {cost:.2f} Rs")
