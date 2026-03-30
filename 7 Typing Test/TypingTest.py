import time
import random

def accuracy(givenstr:str, playerstr:str):
    givenlen = len(givenstr)
    i = 0
    point = 0
    while i < givenlen:
        if i < len(playerstr) and givenstr[i] == playerstr[i]:
            point = point + 1
        i = i + 1
    #Result:
    percentage = (point/givenlen)*100
    return percentage

def wpm(time, user_input):
    split_ver = user_input.split()
    word_count = len(split_ver)

    total = (word_count*60)/time

    return total
 


sentences = ["The brown fox jumps over the lazy dog", 
             "I went to school today and bought home some oranges", 
             "I would really like to build a city for my toys someday", 
             "Why did I have to endure the pain of the loss of a friend?", 
             "Have you bought your stepsisters any presents for our family reunion?", 
             "What's that smell? Did you put on deodorant before we went outside?"]

while True:
    print("""Hello! Welcome to My Typing Test.
        Directions: The test will start when you press 'Y' on your keyboard and enter it.
        After typing, you press enter to end the test. It is graded by how much of your input
        matches the sentence given to you on screen. Do your best and goodluck!\n""")
    ready = input("Are You Ready? (Y/N): ")

    if ready == "Y" or ready == "y":
        random_sentence = random.choice(sentences)
        print(f"{random_sentence}")
        start = time.time()
        user_input = input("START TYPING: ")
        end = time.time()

        total = end - start
        percent = accuracy(random_sentence, user_input)
        word_per_m = wpm(total, user_input)

        print(f"\n\n{total:.2f} Seconds || {percent:.2f}% Accuracy || {word_per_m:.2f} WPM")

        while True:
            exit_input = input("\n\nTry Again? (Y/N): ")
            if exit_input == "Y" or exit_input == "y":
                print("\n")
                break
            elif exit_input == "N" or exit_input == "n":
                quit()
            else:
                print("Invalid Input! Please Try Again")
    elif ready == "N" or ready == "n":
        print("Too bad then :p")
        quit()
    else:
        print("Invalid Input! Please Try Again")

    
