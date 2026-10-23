salary = int(input("Enter your monthly salary: "))
service = int(input("Enter your years of service: "))
rating = input("Enter your performance rating: (excellent/good/average): ").strip().lower()
if (salary >= 50000 and service >= 5) or rating == "excellent":
    print("You are eligible for a bonus.")
else:
    print("You are not eligible for a bonus.")