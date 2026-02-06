gate = 1
while gate == 1:
    print("-------------------------------------------------")
    print("Welcome to my basic calculator program!")
    print("-------------------------------------------------\n")
    num1 = int(input("Enter the 1st Number: "))
    while True:
        opp = input("Enter the operator (+, -, *, /): ")
        if opp == "+" or opp == "-" or opp == "*" or opp == "/":
            break
        else:
            print("You entered an invalid operator, please try again\n")

    num2 = int(input("Enter the 2nd Number: "))
    if opp == "+":
        ans = num1 + num2
    elif opp == "-":
        ans = num1 - num2
    elif opp == "*":
         ans = num1 * num2
    elif opp == "/":
        ans = num1 / num2

    print("\nAnswer: " + str(ans))
    print("-------------------------------------------------")
    while True:
        exitpass = input("Do you wish to exit? (Y/N): ")
        if exitpass == "Y" or exitpass == "y":
            gate = 0
            break
        elif exitpass == "N" or exitpass == "n":
            break
        else:
            print("Your input is invalid, please try again...\n")
