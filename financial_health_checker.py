salary = int(input("Enter your monthly salary: "))
savings = int(input("Enter your monthly savings: "))
expenses = int(input("Enter your monthly expenses: "))
savings_percentage = (savings / salary) * 100
print(f"savings_percentage: {savings_percentage:.2f}%")
if savings_percentage >= 30:
    print("Excellent financial discipline!")
elif 20 <= savings_percentage <30:
    print("Good financial discipline.")
elif 10 <= savings_percentage < 20:
    print("You can improve your savings.")
else:
    print("Your savings rate is low.")