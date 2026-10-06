print("Welcome to the calculator.")
print("This is a basic calculator.")

while True:
    first_input = float(input("Enter the first value: "))
    operator = input("Enter operator: ")
    second_input = float(input("Enter the second value: "))

    if operator == "+":
        print("Ans:", first_input + second_input)

    elif operator == "-":
        print("Ans:", first_input - second_input)

    elif operator == "*":
        print("Ans:", first_input * second_input)

    elif operator == "/":
        if second_input == 0:
            print("Dividing by zero is not possible.")
        else:
            print("Ans:", first_input / second_input)

    elif operator == "**":
        print("Ans:", first_input ** second_input)

    else:
        print("Invalid operator.")

    repeat = input("Do you want another operation? (yes/no)\n").lower()

    if repeat == "yes":
        continue
    else:
        print("Thank you for using the calculator.")
        break
