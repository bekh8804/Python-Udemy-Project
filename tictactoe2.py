class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # Empty line for clarity

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # Ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # Switches player

    if print_game:
        print('It\'s a tie!')


class HumanPlayer:
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input('Choose a square (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


import random


class ComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        # Randomly choose an empty square
        square = random.choice(game.available_moves())
        return square


if __name__ == '__main__':
    x_player = HumanPlayer()
    o_player = ComputerPlayer('O')  # Computer as O
    t = TicTacToe()
    play(t, x_player, o_player)
