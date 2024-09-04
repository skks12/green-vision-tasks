def calculate_animals(heads, legs):
    chickens = (4 * heads - legs) // 2
    dogs = heads - chickens
    return chickens, dogs

heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

chickens, dogs = calculate_animals(heads, legs)

print(f"There are {chickens} chickens and {dogs} dogs.")
