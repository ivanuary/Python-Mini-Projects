import random
import string

def CheckIfInteger(user_input):
    try:
        IntNumber = int(user_input)
        return IntNumber
    except ValueError:
        print("That's not a number! Please Try Again")
        return None
    
def ListMenuChoice(choices:list, num_choice:int, upper, lower, punc, num):
    menu_list = [{"UPPERCASE LETTERS":upper}, {"LOWERCASE LETTERS":lower}, {"PUNCTUATIONS":punc}, {"NUMBERS":num}]
    if  choices.count(menu_list[num_choice-1]) == 1:
        print("You already have this choice!")
    else:
        choices.append(menu_list[num_choice-1])

print("-------------------------------------")
print("Welcome to my password generator!")
print("-------------------------------------")
print("""What would you like your password to consist of?
    1. Uppercase Letters
    2. Lowercase Letters
    3. Punctuations
    4. Numbers""")

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
punctuation_chars = string.punctuation
number_chars = string.digits

menu_choices = []

print("""\nChoose between the 4 choices above :p
      - You can stop choosing by typing 5
      - You can delete a choice by typing 6""")
while True:
    print("-------------------------------------")
    pass_choices = input("Menu Choice: ")
    int_pass_choices = CheckIfInteger(pass_choices)
    if int_pass_choices in [1,2,3,4]:
        ListMenuChoice(menu_choices, int_pass_choices, upper_letters, lower_letters, punctuation_chars, number_chars)
    elif int_pass_choices == 5:
        break
    elif int_pass_choices == 6:
        if len(menu_choices) == 0:
            print("You currently have nothing to remove!")
        else:
            for i, choice in enumerate(menu_choices):
                for key in choice.keys():
                    print(f"{i+1}. {key}")
            while True:
                delete_choice = input("Which choice do you want to remove?: ")
                int_delete_choice = CheckIfInteger(delete_choice)
                if int_delete_choice > len(menu_choices) or int_delete_choice < 1:
                    print("Your choice is not on the list!")
                else:
                    del(menu_choices[int_delete_choice-1])
                    break
    else:
        print("INVALID INPUT, please try again...")
    print("-------------------------------------")
    print("Current Password Generation Settings:")
    for i, choice in enumerate(menu_choices):
        print(f"{i+1}. {choice}")
    print("\nPress 5 to Finish Picking")
    print("Press 6 to Delete a Choice")
pass_combi = ""
for choice in menu_choices:
    for value in choice.values():
        pass_combi += value

full_pass = ""

while True:
    print("How long does your password need to be? (Up to 20 Characters)")
    pass_len = input("ENTER PASSWORD LENGTH: ")
    verified_pass_len = CheckIfInteger(pass_len)
    if verified_pass_len > 20 or verified_pass_len < 1:
        print("You're input is not in the valid range!")
    else:
        for i in range(verified_pass_len):
            rand_char = random.choice(pass_combi)
            full_pass += rand_char
        break

print(f"""Your Generated Password is:
      {full_pass}""")