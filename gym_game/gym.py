import numpy as np


class ActionSpace:
    def __init__(self, n):
        self.n = n


class Game:
    _max_episode_steps = 500
    _steps = 0
    _board_size = 0
    _board = None

    @property
    def state(self):
        return self._board

    def __init__(self, board_size=4):
        self._board_size = board_size
        self.action_space = ActionSpace(board_size)
        self.reset()

    def _is_game_over(self):
        return len(np.where(self._board == 0)[0]) == 0 or self._steps == self._max_episode_steps

    def reset(self):
        self._board = np.zeros(self._board_size)
        self._steps = 0
        return self._board

    def step(self, cell):
        self._steps += 1
        game_over = self._is_game_over()
        if self._board[cell] == 0:
            self._board[cell] = 1
            r = 1
        else:
            r = -1
        return self._board, r, game_over, {}

    def render(self):
        print('-' + '-' * 4 * len(self._board))
        print('|' + '|'.join([' ' + str(int(n)) + ' ' for n in self._board]) + '|')
        print('-' + '-' * 4 * len(self._board))
