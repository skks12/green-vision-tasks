import math

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

gcd = math.gcd(numerator, denominator)

simplified_num = numerator // gcd
simplified_den = denominator // gcd

print(f"The simplified fraction is: {simplified_num}/{simplified_den}")
