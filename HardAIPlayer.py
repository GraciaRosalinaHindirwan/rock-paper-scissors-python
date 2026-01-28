from AIPlayers import AIPlayer
from UserOptions import UserOptions

class HardAIPlayer(AIPlayer):
    def __init__(self, username, opponentPlayer):
        super().__init__(username)
        self.opponentPlayer = opponentPlayer

    def make_choice(self):
        if self.opponentPlayer.choice == UserOptions.ROCK:
            self.choice = UserOptions.PAPER
        elif self.opponentPlayer.choice == UserOptions.PAPER:
            self.choice = UserOptions.SCISSORS
        elif self.opponentPlayer.choice == UserOptions.SCISSORS:
            self.choice = UserOptions.ROCK