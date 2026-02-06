def AddTask(tasks:list):
    print("------------------------------")
    new_task = input("ENTER TASK: ")
    tasks.append(new_task)
    
def ShowTasks(tasks:list):
    print("------------------------------")
    TaskAmount = len(tasks)
    if TaskAmount == 0:
        print("You Currently Have NO Tasks!")
    else:
        print("These are the current tasks you have:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def ModifyOrDeleteTask(tasks:list):
    ShowTasks(tasks)
    TaskAmount = len(tasks)
    print("")
    while True:
        print("------------------------------")
        print("Choose Task to Modify/Delete...")
        ChosenTaskNum = input("ENTER Number: ")
        VerifiedInteger = CheckIfInteger(ChosenTaskNum)
        if VerifiedInteger <= TaskAmount and VerifiedInteger > 0:
            break
        elif VerifiedInteger == 0:
            print("")
        else:
            print("INPUT Item is Not in the Task List, Please Try Again")
    while True:
        print("------------------------------")
        print("Modify (1) or Delete (2)?")
        ModOrDelChoice = input("ENTER Number: ")
        VerifiedChoice = CheckIfInteger(ModOrDelChoice)
        if VerifiedChoice == 1 or VerifiedChoice == 2:
            break
        elif VerifiedChoice == 0:
            print("")
        else:
            print("INVALID Choice, Please Try Again")
    if VerifiedChoice == 1:
        Modify(tasks, VerifiedInteger)
    elif VerifiedChoice == 2:
        Delete(tasks, VerifiedInteger)

def ExitApp(tasks:list):
    while True:
        print("------------------------------")
        ExitConfirm = input("Are You Sure You Want to Exit? (Y/N): ")
        if ExitConfirm == 'Y' or ExitConfirm == 'y':
            SaveTask(tasks)
            quit()
        elif ExitConfirm == 'N' or ExitConfirm == 'n':
            break
        else:
            print("\nINVALID Input! Please Try Again...")

def CheckIfInteger(user_input):
    try:
        IntNumber = int(user_input)
        return IntNumber
    except ValueError:
        print("That's not a number! Please Try Again")
        return 0
    
def Modify(tasks:list, task_num:int):
    print("------------------------------")
    tasks[task_num-1] = input("Enter New Modified Task: ")

def Delete(tasks:list, task_num:int):
    del(tasks[task_num-1])

def SaveTask(tasks:list):
    with open("task_list.txt", "w") as savefile:
        for task in tasks:
            savefile.write(f"{task}\n")

def LoadTask():
    try:
        with open("task_list.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

#Start of Program
#Task List
task_list = LoadTask()

while True:
    print("------------------------------")
    print("To-Do List App")
    print("------------------------------")
    print("""What do you want to do?
        1. Add Task
        2. View Tasks
        3. Modify/Delete Task
        4. Save and Exit App""")
    print("------------------------------")
    #User Chooses an Action
    MenuChoice = input("Enter INPUT: ")
    if MenuChoice == '1':
        AddTask(task_list)
        print("")
    elif MenuChoice == '2':
        ShowTasks(task_list)
        print("")
    elif MenuChoice == '3':
        ModifyOrDeleteTask(task_list)
    elif MenuChoice == '4':
        ExitApp(task_list)
    else:
        print("\nINVALID Input! Please Try Again...")