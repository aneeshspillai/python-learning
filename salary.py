salary = float(input("Enter your monthly salary: "))
pf = float(input("Enter your monthly PF contribution: "))
nps = float(input("Enter your monthly NPS contribution: "))

annual_salary = salary * 12
annual_pf = pf * 12
annual_nps = nps * 12
total_savings = annual_pf + annual_nps
savings_percentage = (total_savings /annual_salary) * 100

print(f"Annual salary: {annual_salary}")
print(f"Annual PF: {annual_pf}")
print(f"Annual nps: {annual_nps}")
print(f"Total annual savings: {total_savings}")
print(f"Savings percentage: {savings_percentage:.2f}%")