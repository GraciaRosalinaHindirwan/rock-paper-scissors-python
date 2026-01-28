import os
from Difficulty import Difficulty

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#fungsi untuk trigger method
def do_player_choice(plenger):
    plenger.make_choice()

def UserDifficulty():
    difficulity = input("Choose your difficulity (easy/normal/hard): ").strip().lower()
    return difficulity

def convertStringToDifficuly():
    difficulty = UserDifficulty()
    if difficulty == "easy":
        return Difficulty.EASY
    elif difficulty == "normal":
        return Difficulty.NORMAL
    else:
        return Difficulty.HARD
