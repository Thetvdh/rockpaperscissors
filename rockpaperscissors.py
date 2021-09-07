import random
import sys


class Game:

    def __init__(self, verbose=False):
        self.possible = ["rock", "paper", "scissors"]
        self.user_input = None
        self.computer_generated = None
        self.verbose = verbose

    def get_human_guess(self):
        while self.user_input is None:
            user_input = str(input("Rock, Paper or Scissors? ").lower().strip())
            if user_input in self.possible:
                self.user_input = user_input

    def generate_computer_guess(self):
        self.computer_generated = random.choice(self.possible)

    def play(self):
        if self.user_input == self.computer_generated:
            print("Draw!" if self.verbose is False else f"Draw! Computer picked \n{self.computer_generated}")
        if self.user_input == self.possible[0] and self.computer_generated == self.possible[1]:
            self.print_output()
            return False
        if self.user_input == self.possible[1] and self.computer_generated == self.possible[2]:
            self.print_output()
            return False
        if self.user_input == self.possible[2] and self.computer_generated == self.possible[0]:
            self.print_output()
            return False
        print("You Win!" if self.verbose is False else f"You Win! Computer picked\n {self.computer_generated}")
        return True

    def print_output(self):
        print(
            "Computer Wins!" if self.verbose is False else f"Computer Wins! "
                                                           f"Computer picked\n {self.computer_generated}")

    def run(self):
        self.generate_computer_guess()
        self.get_human_guess()
        self.play()


def main():
    sys_vars = sys.argv
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        new_game = Game(True) if sys_vars[0] == 'verbose' else Game()
        new_game.run()
        if input("Play again? Y/N").lower() == 'y':
            del new_game
        else:
            sys.exit()


if __name__ == '__main__':
    main()
