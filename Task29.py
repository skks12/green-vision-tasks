def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

print("Armstrong numbers between 100 and 1000 are:")
for i in range(100, 1000):
    if is_armstrong(i):
        print(i, end=" ")
