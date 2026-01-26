import random
from Player import Player
from UserOptions import UserOptions

class AIPlayer(Player):
    def make_choice(self):
        self.choice = random.choice(UserOptions.toList())
        print(f"your opponent: {self.choice}")