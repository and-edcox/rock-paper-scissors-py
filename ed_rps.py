import json
import random as rand
import os


class RockPaperScissors:
    def __init__(self):
        # Define win conditions dict - keys are winners, values are losers
        self.win_conditions = win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock",
        }

        # Check to see if game history exists, if not initialise
        if not os.path.exists("rps_history.json"):
            self.history = {}
        else:
            with open("rps_history.json") as f:
                self.history = json.load(f)

    def add_player(self, player):
        # Add player to game history dict
        self.history[player.lower()] = {"win": 0, "loss": 0, "draw": 0}

    def update_score(self, player, result):
        # Update players game history
        self.history[player.lower()][result] += 1

    def display_score(self, player):
        # Display players game history
        print("Here is your game history:\n")
        for result, total in self.history[player.lower()].items():
            print(f"{result.capitalize()}:\t {total}")

    def save_score(self):
        # Save game history to JSON file
        with open("rps_history.json", "w") as f:
            json.dump(self.history, f)

    def engine(self, player):
        # Generate list of possible moves from win conditions dict
        possible_moves = list(self.win_conditions.keys())

        while True:
            # Player selects move
            print(f"Please choose from the following: {', '.join(possible_moves)}")
            go = input()

            if go.lower() in possible_moves:
                # Computer randomly generated move
                comp_go = possible_moves[rand.randint(0, len(possible_moves) - 1)]

                # Check to see if player has won and update scores
                if self.win_conditions[go] == comp_go:
                    self.update_score(player, "win")
                    print(f"You win! {go} beats {comp_go}")

                # Check to see if computer has won and update scores
                elif self.win_conditions[comp_go] == go:
                    self.update_score(player, "loss")
                    print(f"You lose :( {comp_go} beats {go}")

                # Check for draw and update scores
                else:
                    self.update_score(player, "draw")
                    print("It's a draw :/")

                # Ask to play again
                while True:
                    print("\nWould you like to play again?")
                    decision = input("Y/n")
                    if not decision or decision == "y":
                        break
                    elif decision == "n":
                        self.save_score()
                        return
                    else:
                        print("Invalid input.")

            # Invalid move check
            else:
                print("Invalid input.")

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!\n")

        # Ask for players name and retrieve game history
        print("What's your name?")
        player = input()

        if player.lower() in self.history:
            print("\nI see you've played before!\n")
            self.display_score(player)
        else:
            self.add_player(player)

        # Ask player if they'd like to start a new game
        print("\nWould you like to play?")
        decision = input("Y/n")

        while True:
            # Start game
            if not decision or decision.lower() == "y":
                print("\nStarting game...\n")
                self.engine(player)
                self.display_score(player)
                print("\nThanks for playing!")
                return

            # End game
            elif decision.lower() == "n":
                print("\nSee you later!")
                return

            # Invalid input check
            else:
                print("Invalid input.")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
