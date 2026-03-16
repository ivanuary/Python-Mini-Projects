import csv
# Functions
# Check if the input is an integer
def CheckIfInteger(user_input):
    try:
        IntNumber = int(user_input)
        return IntNumber
    except ValueError:
        print("That's not a number! Please Try Again")
        return 'Invalid'

# Add An Expense Entry
def WriteExpense(expense_list:list):
    print("""ENTRY FORMAT: 
[DATE, CATEGORY, DESCRIPTION, AMOUNT(PHP)]""")
    header_columns = ["DATE(MM/DD/YYYY)", "CATEGORY", "DESCRIPTION", "AMOUNT(PHP)"]
    row_inputs = []
    for header in header_columns:
        print(f"\nENTER {header}:")
        row_entry = input("")
        rowentry_upper = row_entry.upper()
        row_inputs.append(rowentry_upper)
    
    expense_list.append(row_inputs)

# View Expense Entries
def ViewExpenses(expense_list:list):
    list_count = len(expense_list)
    if list_count == 0:
        print("You Currently Have No Expense Entries!")
    else:
        print("   |  DATE  |  CATEGORY  |  DESCRIPTION  |  AMOUNT  |")
        for i, row in enumerate(expense_list):
                print(f"{i+1}: {row}")

# Delete Expense Log
def ModifyOrDeleteLog(expense_list:list):
    ViewExpenses(expense_list)
    list_count = len(expense_list)
    if list_count == 0:
        return
    else:
        while True:
            print("--------------------------------")
            LogInput = input("Which Entry Do You Want to Modify/Delete?: ")
            VerifiedLogInput = CheckIfInteger(LogInput)
            if VerifiedLogInput != 'Invalid':
                if VerifiedLogInput > list_count or VerifiedLogInput < 1:
                    print("INVALID INPUT, Please Pick from the Available Rows")
                else:
                    while True:
                        ("--------------------------------")
                        ModOrDeleteInput = input("Modify (1) or Delete (2)?: ")
                        if ModOrDeleteInput == '1':
                            new_expense = []
                            header_columns = ["DATE(MM/DD/YYYY)", "CATEGORY", "DESCRIPTION", "AMOUNT(PHP)"]
                            for header in header_columns:
                                print(f"\nENTER {header}:")
                                row_entry = input("")
                                rowentry_upper = row_entry.upper()
                                new_expense.append(rowentry_upper)
                                
                            expense_list[VerifiedLogInput-1] = new_expense
                            return
                        elif ModOrDeleteInput == '2':
                            del(expense_list[VerifiedLogInput-1])
                            print(f"Row {VerifiedLogInput} has been deleted!")
                            return
                        else:
                            print("INVALID INPUT, Please Try Again")

# Exit Program
def ExitTracker(expense_list:list):
    while True:
        ExitConfirm = input("Are you sure you want to exit?(Y/N): ")
        if ExitConfirm == 'y' or ExitConfirm == 'Y':
            SaveTrack(expense_list)
            quit()
        elif ExitConfirm == 'N' or ExitConfirm == 'n':
            break
        else:
            print("Invalid Input, Please Try Again...")
            print("--------------------------------")
    
# Save Expense List for Future Use
def SaveTrack(expense_list:list):
    with open("expense_track.csv", "w", newline='') as expense_file:
        file_writer = csv.writer(expense_file)
        file_writer.writerow(["DATE", "CATEGORY", "DESCRIPTION", "AMOUNT"])
        for row in expense_list:
            file_writer.writerow(row)

# Load Expense List for Future Use
def LoadTrack():
    try:
        with open("expense_track.csv", "r") as expense_file:
            csv_track = csv.reader(expense_file)
            next(csv_track)
            expense_import = []
            for row in csv_track:
                expense_import.append(row)
            return expense_import
    except FileNotFoundError:
        return []


# Start of Program
expense_list = LoadTrack()
while True:
    print("--------------------------------")
    print("Simple Expense Tracker!")
    print("--------------------------------")
    print("""What Would You Like To Do?
        1. Add Expense Log
        2. View Expense Log
        3. Modify or Delete Expense Log
        4. Save & Exit Expense Tracker""")
    print("--------------------------------")
    MenuChoice = input("INPUT MENU OPTION: ")
    print("--------------------------------")
    
    if MenuChoice == '1':
        WriteExpense(expense_list)
    elif MenuChoice == '2':
        ViewExpenses(expense_list)
    elif MenuChoice == '3':
        ModifyOrDeleteLog(expense_list)
    elif MenuChoice == '4':
        ExitTracker(expense_list)
    else:
        print("Invalid Input, Please Try Again")

# End of Program