import random
import colorama
from colorama import Fore 

colorama.init()
print(Fore.GREEN)

"""This program will simulate the game of Rock, Paper, Scissors but with theme of the movie "The Matrix..." """

class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input("Rock, Paper, Scissors? > ")
            if move_human.lower() in self.moves:
                return move_human.lower()
            elif move_human.lower() == 'exit':
                exit()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.score_p1 = 0
        self.score_p2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def rounds(self):
        while True:
            self.number_rounds = input(
                "How many rounds do you want want play? The Oracle thinks you'll play 10... > ")
            if self.number_rounds.isdigit():
                return self.number_rounds
            elif self.number_rounds.lower() == 'exit':
                exit()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        
        if self.beats(move1, move2):
            self.score_p1 += 1
            winner = '>>>> Neo Wins! <<<<'
        elif move1 == move2:
            self.score_p1 = self.score_p1
            self.score_p2 = self.score_p2
            winner = '>>>> Tie <<<<'
        else:
            self.score_p2 += 1
            winner = '>>>> Agent Smith Wins! <<<<'
        
        print(
            f"> Neo played : {move1}"
            f"\n> Agent Smith played : {move2}"
            f"\n{winner}"
            f"\nScore: Neo ( {self.score_p1} ),"
            f"Agent Smith ( {self.score_p2} )"
        )
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(
            "Hello Neo... want to enter The Matrix? All you need to do is beat Agent Smith in Rock, Paper, Scissors..."
        )
        self.rounds()
        for round in range(int(self.number_rounds)):
            print(f"\nRound {round + 1} -")
            self.play_round()
        if self.score_p1 == self.score_p2:
            print(
                f"\n>>>>The game ended in a tie... Restart the Simulation!!<<<<"
                f"\nScore: Neo ( {self.score_p1} ),"
                f"Agent Smith ( {self.score_p2} )"
            )
        elif self.score_p1 > self.score_p2:
            print(
                f"\n>>>>YOU DID IT NEO YOU WON, YOU'RE BEGGINING TO BELEIVE<<<<"
                f"\nThe Matrix has you..."
                f"\nScore: Neo ( {self.score_p1} )*,"
                f"Agent Smith ( {self.score_p2} )"
            )
        else:
            print(
                f"\n>>>>AGENT SMITH HAS WON<<<<"
                f"\n>>>>ACCESS TO THE MATRIX IS DENIED!<<<<"
                f"\nScore: Neo ( {self.score_p1} ),"
                f"Agent Smith ( {self.score_p2} )*"
            )

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()