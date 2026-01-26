import os
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#fungsi untuk trigger method
def do_player_choice(plenger):
    plenger.make_choice()

