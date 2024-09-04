def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
num = 2
primes = []

while count < 25:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1

print("First 25 prime numbers are:", primes)
