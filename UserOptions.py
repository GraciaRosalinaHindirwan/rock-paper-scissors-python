from enum import Enum

class UserOptions(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @classmethod
    def toList(cls):
        return [option.value for option in cls] #mengembalikan user opt jadi list ["rock", "paper", "scissors"]
