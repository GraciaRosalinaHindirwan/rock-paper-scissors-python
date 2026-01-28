from utils import clear, UserDifficulty, convertStringToDifficuly
import Player
import AIPlayers
from Difficulty import Difficulty
from HardAIPlayer import HardAIPlayer

#objek
user_1 = Player.Player("user1")

print("=============================")
print("         Welcome To          ")
print(" Rock–Paper–Scissors Classic ")
print("=============================")
print("\n")
input("Enter to continue...")

repeat = True

clear()
difficult = convertStringToDifficuly()
if difficult == Difficulty.EASY or difficult == Difficulty.NORMAL:
    AI_1 = AIPlayers.AIPlayer("AI_1")
else:
    AI_1 = HardAIPlayer("AI_1", user_1)

while repeat:
    print("You’ll play this game 3 times in a row!")
    print("\n")


    for i in range(1,4):
        print(f"Round: {i}/3")
        user_1.battle(AI_1)
    

    #Loop the game
    print("\n")
    while True:
        repeat = input("Do you want to play again? [yes/no]: ").strip().lower() #agar inputan user lower semua
        if repeat == "yes":
            repeat = True
            print("Current session score will continue.")
            input("Enter to continue...")

        elif repeat == "no":
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
        else:
            print("Invalid Input...")


    