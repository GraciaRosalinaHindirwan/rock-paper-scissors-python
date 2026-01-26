from utils import clear
import players

#objek
user_1 = players.User("user1")
AI_1 = players.AIPlayer("AIPlayer")

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
        user_1.make_choice()
        AI_1.random_choice()
                
        if user_1.choice == AI_1.choice:  # membandingkan nilai acak dengan inputan user
            print("FAIR")
        elif (
            (user_1.choice == "rock" and AI_1.choice == "scissors")
            or (user_1.choice == "scissors" and AI_1.choice == "paper")
            or (user_1.choice == "paper" and AI_1.choice == "rock")
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