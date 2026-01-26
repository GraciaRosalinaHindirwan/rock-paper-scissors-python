import random

moves = ["rock", "paper", "scissors"]
class User:
    def __init__(self, username):
        self.username = username
        self.choice = None
    
    def make_choice(self):
        while True:
            self.choice = input("Enter your Choice [rock, paper, scissors]: ")
            if self.choice == self.choice.strip().lower() and self.choice in moves:
                break
            else:
                print("Invalid move! Choose rock, paper, or scissors!")


class AIPlayer:
    def __init__(self, name):
        self.name = "AIPlayer"
        self.choice = None 
        self.AImoves = moves
    
    def random_choice(self):
        self.choice = random.choice(self.AImoves)
        print(f"your opponent: {self.choice}")