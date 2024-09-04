population = 10000
rate = 10  # 10% per year

print("Population at the end of each year for the last 10 years:")
for year in range(10, 0, -1):
    print(f"{year}th year - {population}")
    population = int(population / (1 + rate / 100))
