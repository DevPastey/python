import abc
import random

class Player(abc.ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        new_x = self.position[0]+ move[0]
        new_y = self.position[1]+ move[1]
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position
    
    @abc.abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        # Define basic 1-unit movements (Up, Down, Left, Right)
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def level_up(self):
        # Add diagonal movements to the existing moves list
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)