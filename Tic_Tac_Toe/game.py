import time
from player import Human_player, Computer_player, Genius_computer


class Tictactoe:
    def __init__(self):
        self.board =[' ' for _ in range(9)]     # Single list to represent 3x3 board
        self.current_winner = None      # Keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    # Define numbers for each box in the board(| 0 | 1 | 2 |)
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # Check for availbe spots and give number
    def available_moves(self):
        return (i for i, spot in enumerate(self.board) if spot == ' ')
    
    # Check if there are empty boxes
    def empty_squares(self):
        return ' ' in self.board

    # Count number of empty boxes
    def empty_squares_count(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Check for 3 in a row in any direction ( horizontal, vertical and diagonal)
    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonal
        # only moves possible are 0, 2, 4, 6, 8
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]      # Top left to bottom right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]      # Top right to bottom left
            if all([spot == letter for spot in diagonal2]):
                return True

        # If everything fails, no winner
        return False


def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_numbers()
    
    letter = 'X'
    # Get move from player
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # Make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            # Print Winner
            if game.current_winner:
                if print_game:
                    print(letter + " wins !!")
                return letter
            
            letter = 'O' if letter == 'X' else 'X'      # Switching player
        
        # Add a wait time for clarity
        time.sleep(0.8)

    if print_game:
        print("It's a tie !! 🤨")

if __name__ == '__main__':
    x_player = Human_player('X')
    o_player = Genius_computer('O')
    t = Tictactoe()
    play(t, x_player, o_player, print_game=True)
