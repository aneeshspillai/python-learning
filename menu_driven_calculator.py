while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    menu_selection = int(input("Select an option (1-5): "))
    if menu_selection == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        total = num1 + num2
        print("The total is : ", total)
    elif menu_selection == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        difference = num1 - num2
        print("The difference is : ", difference)
    elif menu_selection == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        multiplication = num1*num2
        print("The multiplication is : ", multiplication)
    elif menu_selection == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            division = num1/num2
            print("The division is : ", division)
    elif menu_selection == 5:
        print("Goodbye!")
        break
    else:
        print("Please select a valid option")