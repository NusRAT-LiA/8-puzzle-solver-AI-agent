import numpy as np
from random import randint, choice

class Pad:
    def __init__(self):
        self.board = np.arange(9).reshape(3, 3)

    def swap(self, a, b):
        self.board[a], self.board[b] = self.board[b], self.board[a]

    def find_zero(self):
        return np.argwhere(self.board == 0)[0]

    def move(self, direction):
        zero_pos = self.find_zero()
        move_offsets = {
            'left': (0, 1),
            'right': (0, -1),
            'up': (1, 0),
            'down': (-1, 0)
        }
        offset = move_offsets[direction]
        new_pos = zero_pos + np.array(offset)

        if not (0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3):
            return False

        self.swap(tuple(zero_pos), tuple(new_pos))
        return True

    def move_left(self):
        return self.move('left')

    def move_right(self):
        return self.move('right')

    def move_up(self):
        return self.move('up')

    def move_down(self):
        return self.move('down')

    def __str__(self):
        return '\n'.join(['| ' + ' | '.join(str(int(x)) if x != 0 else ' ' for x in row) + ' |' for row in self.board])+'\n'

    def shuffle(self):
        for _ in range(randint(10, 100)):
            choice([self.move_down, self.move_up, self.move_right, self.move_left])()

    def apply_chain(self, chain, with_display=False):
        chain_map = {
            'up': self.move_up,
            'down': self.move_down,
            'left': self.move_left,
            'right': self.move_right
        }
        for direction in chain:
            chain_map[direction]()
            if with_display:
                print(self)

    def cost(self):
        reference = np.arange(9).reshape(3, 3)
        error = 0.0

        for val in range(9):
            index = np.argwhere(self.board == val)[0]
            ref_index = np.argwhere(reference == val)[0]
            error += np.sum((index - ref_index) ** 2)

        return error / 9.0
