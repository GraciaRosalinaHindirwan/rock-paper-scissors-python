import UserOptions

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
