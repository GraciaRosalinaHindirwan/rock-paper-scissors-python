import random
from utils import clear

choices = ["rock", "paper", "scissors"]

print("=============================")
print("         Welcome To          ")
print(" Rock–Paper–Scissors Classic ")
print("=============================")
print("\n")
input("Enter to continue...")

score_user = 0
score_computer = 0
repeat = True

clear()
while repeat:
    print("You’ll play this game 3 times in a row!")
    print("\n")
    for i in range(1,4):
        print(f"Round: {i}/3")
        while True: #looping untuk error handling
            user = input("Enter your Choice [rock, paper, scissors]: ")
            user = user.strip().lower()
            if user in choices:
                break
            else:
                print("Invalid move! Choose rock, paper, or scissors!")

        computer = random.choice(choices)  # nilai acak disimpan ke dalam variabel computer
        print(f"Your opponent chooses: {computer}")

        if user == computer:  # membandingkan nilai acak dengan inputan user
            print("FAIR")
        elif (
            (user == "rock" and computer == "scissors")
            or (user == "scissors" and computer == "paper")
            or (user == "paper" and computer == "rock")
            ):
            print("WIN")
            score_user += 1
        else:
            print("LOSE")
            score_computer += 1

    #Loop the game
    print("\n")
    repeat = input("Do you want to play again? [yes/no]: ").strip().lower() #agar inputan user lower semua
    if repeat == "yes":
        print("Current session score will continue.")
        input("Enter to continue...")
        repeat = True
    else:
        repeat = False
        clear()
        print("====  GAME RESULT  ====")
        print(f"Your Score: {score_user}")
        print(f"Your opponent Score: {score_computer}")
        print("\n")

        if score_user > score_computer:
            print("=============================")
            print("         YOU WIN!!!          ")
            print("=============================")
            print("\n")
        elif score_user == score_computer:
            print("=============================")
            print("        T'S A DRAW           ")
            print("=============================")
            print("\n")
        else:
            print("=============================")
            print("         YOU LOSE!!!         ")
            print("=============================")
            print("\n")
        
        print("Thankyou for Playing. Byee")
        break