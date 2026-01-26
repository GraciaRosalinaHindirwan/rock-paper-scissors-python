moves = ["rock", "paper", "scissors"]
class user:
    def __init__(self, username, choice):
        self.username = username
        self.choice = None
    
    def make_choice():
        while True:
            self.choice = input("Enter your Choice [rock, paper, scissors]: ")
            self.choice = self.choice.strip().lower()
            if self.choice in moves:
                break
            else:
                print("Invalid move! Choose rock, paper, or scissors!")


class AIPlayer:
    def __init__(self, name, choice, AImoves):
        self.name = "AIPlayer"
        self.AIchoice = None 
        self.AImoves = moves
    
    def random_choice():
        self.AIchoice = random.choice(AI.moves)