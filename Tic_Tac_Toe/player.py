import math
import random

class Player:
    def __init__(self, letter):     # letter is X or O
        self.letter = letter
    
    # Get the players next move
    def get_move(self, game):
        pass

class Computer_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get a random valid spot
    def get_move(self, game):
        square = random.choice(list(game.available_moves()))        # Convert to a list, otherwise get an 'TypeError'
        return square

class Human_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8): ")
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True     # If the value is correct. No problem.
            except ValueError:
                print("Invaild Square, try again 😉 ")
        
        return val
    
class Genius_computer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(list(game.available_moves())) == 9:
            square = random.choice(list(game.availble_moves()))
        else:
            square = self.minimax(game, self.letter)['position']       # Get square from minimax algorithm
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # This is base case
        if state.current_winner == other_player:
            return{'position': None,
                    'score': 1 * (state.empty_squares_count() + 1) if other_player == max_player else -1 * (
                        state.empty_squares_count() + 1)
                }
        elif not state.empty_squares():
            return{'position': None,
                    'score': 0
                }
        
        if player == max_player:
            best = {'position': None,
                    'score': -math.inf
                }
        else:
            best = {'position': None,
                    'score': math.inf
                }
        
        for possible_move in state.available_moves():
            # Make a move and try a spot
            state.make_move(possible_move, player)

            # Simulation using minimax
            simulation_score = self.minimax(state, other_player)

            # Reset
            state.board[possible_move] = ' '
            state.current_winner = None
            simulation_score['position'] = possible_move

            # Update dictionaties
            if player == max_player:
                if simulation_score['score'] > best['score']:
                    best = simulation_score
            else:
                if simulation_score['score'] < best['score']:
                    best = simulation_score
            
        return best
