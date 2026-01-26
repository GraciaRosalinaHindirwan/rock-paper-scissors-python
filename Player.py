import UserOptions
from utils import do_player_choice

class Player:
    def __init__(self, username):
        self.username = username
        self.choice = None
        self.score = 0
    
    def make_choice(self):
        while True:
            self.choice = input("Enter your Choice [rock, paper, scissors]: ")
            if self.choice == self.choice.strip().lower() and self.choice in UserOptions.UserOptions.toList():
                break
            else:
                print("Invalid move! Choose rock, paper, or scissors!")

    def battle(self, opponent):
        do_player_choice(self)
        do_player_choice(opponent)
        if self.choice == opponent.choice:  # membandingkan nilai acak dengan inputan user
            print("FAIR")
        elif (
            (self.choice == "rock" and opponent.choice == "scissors")
            or (self.choice == "scissors" and opponent.choice == "paper")
            or (self.choice == "paper" and opponent.choice == "rock")
            ):
            print("WIN")
            self.score += 1
        else:
            print("LOSE")
            opponent.score += 1


