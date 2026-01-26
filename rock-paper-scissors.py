from utils import clear, do_player_choice
import Player
import AIPlayers

#objek
user_1 = Player.Player("user1")
AI_1 = AIPlayers.AIPlayer("AIPlayer")

print("=============================")
print("         Welcome To          ")
print(" Rock–Paper–Scissors Classic ")
print("=============================")
print("\n")
input("Enter to continue...")

repeat = True

clear()
while repeat:
    print("You’ll play this game 3 times in a row!")
    print("\n")
    
    for i in range(1,4):
        print(f"Round: {i}/3")
        user_1.battle(AI_1)
    

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
        print(f"Your Score: {user_1.score}")
        print(f"Your opponent Score: {AI_1.score}")
        print("\n")

        if user_1.score > AI_1.score:
            print("=============================")
            print("         YOU WIN!!!          ")
            print("=============================")
            print("\n")
        elif user_1.score == AI_1.score:
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