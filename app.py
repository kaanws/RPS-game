import random
def cheat_ai_choice(users_choice):
    if users_choice == "Rock":
        return "Paper"
    elif users_choice == "Paper":
        return "Scissors"
    else:
        return "Rock"
def produce_ai_choice():
    n = random.randint(1,3)
    if n == 1:
        return "Rock"
    elif n == 2:
        return "Paper"
    else:
        return "Scissors"
score_ai = 0
score_user = 0

while True:
    users_choice = input("Rock? Paper? Scissors? ")
    n = random.randint(1,2)
    if n == 1:
        ai_choice = produce_ai_choice()
    else:
        ai_choice = cheat_ai_choice(users_choice)

    print("PC: ", ai_choice)

    if users_choice == ai_choice:
        print("Draw")
    elif users_choice == "Paper" and ai_choice == "Rock":
        score_user += 1
    elif users_choice == "Paper" and ai_choice == "Scissors":
        score_ai += 1
    elif users_choice == "Rock" and ai_choice == "Scissors":
        score_user += 1
    elif users_choice == "Rock" and ai_choice == "Paper":
        score_ai += 1
    elif users_choice == "Scissors" and ai_choice == "Paper":
        score_user += 1
    else:
        score_ai += 1

    print("You: ", score_user, "VS PC: ", score_ai)

    if score_ai == 3 or score_user == 3:
        break

if score_ai > score_user:
    print("Computer Wins!")
else:
    print("You Win!")
