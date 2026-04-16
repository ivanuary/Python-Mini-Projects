import random
guess_num = random.randint(1, 50)
print(guess_num)
round = 0
while round < 5:
    user = int(input("Enter Guess: "))
    abs_ans = abs(guess_num - user)
    if user == guess_num:
        print("Congrats!")
        break
    elif abs_ans < 5:
        print("Hot!")
    elif abs_ans < 10:
        print("Warm!")
    elif abs_ans > 10:
        print("Cold")
    round += 1
if round == 5:
    print("Sorry Try Again Next Time!")