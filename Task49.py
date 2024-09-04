sum_numbers = 0
count = 0

while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    sum_numbers += num
    count += 1

if count == 0:
    print("No numbers were entered.")
else:
    average = sum_numbers / count
    print(f"The sum of the numbers is: {sum_numbers}")
    print(f"The average of the numbers is: {average}")
