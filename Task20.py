def calculate_in_hand_salary(salary):
    HRA = 0.10 * salary
    DA = 0.05 * salary
    PF = 0.03 * salary
    
    salary_after_deductions = salary - (HRA + DA + PF)
    
    if salary > 2000000:
        tax = 0.30 * salary
    elif salary > 1000000:
        tax = 0.20 * salary
    elif salary > 500000:
        tax = 0.10 * salary
    else:
        tax = 0
    
    in_hand_salary = salary_after_deductions - tax
    return in_hand_salary

salary = float(input("Enter your salary: "))
in_hand = calculate_in_hand_salary(salary)

if salary <= 100000:
    print("Salary in hand: K")
else:
    print(f"Salary in hand: {in_hand}")
