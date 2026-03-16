import random as rand
print("-----------------------------------")
print("Welcome to my number guessing game!")
print("-----------------------------------")
print('''Instructions:
    The player must guess the number between 1 to 100,
    within 8 guesses. The less guesses you take to guess
    the number, the more points you get!
      
    Any guesses made will be final, so be careful when guessing!''')
print("-----------------------------------")
guessnum = rand.randint(1,100)
print("The Computer has now chosen a number, you may now guess between 1 - 100")
roundnum = 1
winnum = 0
while roundnum < 9:
    print("-----------------------------------")
    print("Guess #" + str(roundnum) + "!")
    while True:
        guessinput = str(input("Input a Number Between 1-100: "))
        guessstrip = guessinput.strip()
        if guessstrip.isdigit():
            guess = int(guessstrip)
            break
        else:
            print("What You Entered Was not an Integer! Please Enter an Integer...\n")
    
    range = abs(guessnum - guess)
    if range == 0:
        winnum = 1
        break
    elif range <= 5:
        print("\nYou are Burning! (5 Unit Range)")
    elif range <= 10:
        print("\nYou are On Fire! (10 Unit Range)")
    elif range <=15:
        print("\nYou're Pretty Cold! (15 Unit Range)")
    else:
        print("\nYou're Freezing! (More Than 15 Units)")
    
    roundnum = roundnum + 1

if winnum == 1:
    print("Congrats! You guessed correctly!")
else:
    print("The 8 Guesses are over! The number was " + str(guessnum))

