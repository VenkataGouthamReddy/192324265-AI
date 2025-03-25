print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid Input")

    # Ask user if they want to perform another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
