def xturn(a):
    checkstat = 0
    while checkstat == 0:
        xbox = int(input("Enter the box you will put X in: ")) - 1
        checkstat = checkbox(a, xbox)
        if checkstat == 1:
            break
    a[xbox] = "X"
    print("\n+---+---+---+")
    print("| " + boxes[0] + " | " + boxes[1] + " | " + boxes[2] + " |")
    print("+---+---+---+")
    print("| " + boxes[3] + " | " + boxes[4] + " | " + boxes[5] + " |")
    print("+---+---+---+")
    print("| " + boxes[6] + " | " + boxes[7] + " | " + boxes[8] + " |")
    print("+---+---+---+\n")

def oturn(b):
    checkstat = 0
    while checkstat == 0:
        obox = int(input("Enter the box you will put O in: ")) - 1
        checkstat = checkbox(b, obox)
        if checkstat == 1:
            break
    b[obox] = "O"
    print("\n+---+---+---+")
    print("| " + boxes[0] + " | " + boxes[1] + " | " + boxes[2] + " |")
    print("+---+---+---+")
    print("| " + boxes[3] + " | " + boxes[4] + " | " + boxes[5] + " |")
    print("+---+---+---+")
    print("| " + boxes[6] + " | " + boxes[7] + " | " + boxes[8] + " |")
    print("+---+---+---+\n")

def checkbox(d, e):
    if e > 8 or e < 0:
        print("Invalid Box Number, Choose from 1-9\n")
        return 0
    else:
        if d[e] != " ":
            print("This box is not empty, please pick an empty box\n")
            return 0
        else:
            return 1

def point(c):
    if c[0] == c[1] == c[2] == "X":
        return 1
    elif c[3] == c[4] == c[5] == "X":
        return 1
    elif c[6] == c[7] == c[8] == "X":
        return 1
    elif c[0] == c[3] == c[6] == "X":
        return 1
    elif c[1] == c[4] == c[7] == "X":
        return 1
    elif c[2] == c[5] == c[8] == "X":
        return 1
    elif c[0] == c[4] == c[8] == "X":
        return 1
    elif c[2] == c[4] == c[6] == "X":
        return 1
    elif c[0] == c[1] == c[2] == "O":
        return 2
    elif c[3] == c[4] == c[5] == "O":
        return 2
    elif c[6] == c[7] == c[8] == "O":
        return 2
    elif c[0] == c[3] == c[6] == "O":
        return 2
    elif c[1] == c[4] == c[7] == "O":
        return 2
    elif c[2] == c[5] == c[8] == "O":
        return 2
    elif c[0] == c[4] == c[8] == "O":
        return 2
    elif c[2] == c[4] == c[6] == "O":
        return 2
    else:
        return 0

exitnum = 1
while exitnum == 1:
    print("-------------------------------------")
    print("Welcome to my Tic Tac Toe Game!")

    print("\n+---+---+---+")
    print("| 1 | 2 | 3 |")
    print("+---+---+---+")
    print("| 4 | 5 | 6 |")
    print("+---+---+---+")
    print("| 7 | 8 | 9 |")
    print("+---+---+---+")
    print("This is what the bored currently looks like!\n")
    print("It's X's Turn")

    boxes = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]

    winner = 0
    counter = 0
    while winner == 0:
        xturn(boxes)
        winner = point(boxes)
        if winner != 0:
            break
        counter += 1
        if counter == 9:
            break

        oturn(boxes)
        winner = point(boxes)
        if winner != 0:
            break
        counter += 1
        if counter == 9:
            break

    if winner == 1:
        print("Congrats, X Wins!\n")
        print("Do you wish to Exit[0] or Play Again[1]?")
        while True:
            exitnum = int(input("Input here: "))
            if exitnum == 1 or exitnum == 0:
                break
            else:
                print("Your input is INVALID, try again...")
    elif winner == 2:
        print("Congrats, O Wins!")
        print("Do you wish to Exit[0] or Play Again[1]?")
        while True:
            exitnum = int(input("Input here: "))
            if exitnum == 1 or exitnum == 0:
                break
            else:
                print("Your input is INVALID, try again...")
    elif counter == 9:
        print("No One Won That Round!")
        print("Do you wish to Exit[0] or Play Again[1]?")
        while True:
            exitnum = int(input("Input here: "))
            if exitnum == 1 or exitnum == 0:
                break
            else:
                print("Your input is INVALID, try again...")

    if exitnum == 0:
        break
quit()
    