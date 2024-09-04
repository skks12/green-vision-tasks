def find_oldest(age1, age2, age3):
    return max(age1, age2, age3)

age1 = int(input("Enter the first age: "))
age2 = int(input("Enter the second age: "))
age3 = int(input("Enter the third age: "))
print("The oldest age is:", find_oldest(age1, age2, age3))
