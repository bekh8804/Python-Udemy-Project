import os

os.system('clear')


class GameBoard:
    def __init__(self):
        self.set_up = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    @staticmethod
    def print_header():
        print("Welcome to Tic-Tac-Toe\n")

    def display(self):
        print(f" {self.set_up[1]}  |  {self.set_up[2]}  |  {self.set_up[3]} ")
        print("---------------")
        print(f" {self.set_up[4]}  |  {self.set_up[5]}  |  {self.set_up[6]} ")
        print("---------------")
        print(f" {self.set_up[7]}  |  {self.set_up[8]}  |  {self.set_up[9]} ")

    def display_update(self, num, player):
        self.set_up[num] = player

    def clear_board(self):
        self.set_up = self.set_up = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        return print("All clear")

    def refresh_display(self):
        os.system("clear")
        self.print_header()
        self.display()

    def is_win(self, player):
        # Check rows
        for i in range(1, 8, 3):
            if self.set_up[i] == self.set_up[i + 1] == self.set_up[i + 2] == player:
                return True

        # Check columns
        for i in range(1, 4):
            if self.set_up[i] == self.set_up[i + 3] == self.set_up[i + 6] == player:
                return True

        # Check diagonals
        if self.set_up[1] == self.set_up[5] == self.set_up[9] == player:
            return True
        if self.set_up[3] == self.set_up[5] == self.set_up[7] == player:
            return True

        return False

    def is_tie(self):
        count = 0
        for i in range(1, 10):
            if self.set_up[i] != ' ':
                count += 1
        if count == 9:
            return True
        return False


class Player:
    def __init__(self, player_name):
        self.player_name = player_name

    def player_choice(self):
        return int(input(f"{self.player_name}) Choose between 1-9"))

    def player_won(self):
        print(f'Player {self.player_name} won')

    @staticmethod
    def players_tie():
        print("Its a tie")

    @staticmethod
    def play_again_ask():
        return input("Wanna play again? Y/N")

    def play_again(self, answer):
        if answer == 'Y':
            return True
        return False




my_game = GameBoard()
my_game.display()

player1 = Player('X')
player2 = Player('Y')
while True:

    my_game.refresh_display()

    position1 = player1.player_choice()
    my_game.display_update(position1, player1.player_name)

    if my_game.is_win(player1.player_name):
        player1.player_won()
        answer = player1.play_again(player1.play_again_ask())  # Call play_again method here
        if player1.play_again(answer):
            my_game.clear_board()
        else:
            break
    if my_game.is_tie():
        player1.players_tie()
        answer = player1.play_again(player1.play_again_ask())  # Call play_again method here
        if player1.play_again(answer):
            my_game.clear_board()
        else:
            break

