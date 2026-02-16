def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please try again.")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break


calculator()
