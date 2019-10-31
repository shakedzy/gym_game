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
        r = -1 if self._board[cell] == 0 else 1
        self._board[cell] = 1
        game_over = self._is_game_over()
        return self._board, r, game_over, {}

    def render(self, line_break=10):
        def print_single_line(line): print('|' + '|'.join([' ' + str(int(n)) + ' ' for n in line]) + '|')
        def print_bars(line): print('-' + '-' * 4 * len(line))
        if self._board_size <= line_break:
            print_bars(self._board)
            print_single_line(self._board)
            print_bars(self._board)
        else:
            last_line = None
            brd = np.copy(self._board)
            if self._board_size % line_break != 0:
                idx = self._board_size // line_break * line_break
                last_line = brd[idx:]
                brd = brd[:idx]
            brd = brd.reshape((-1, line_break))
            print_bars(brd[0])
            for line in brd:
                print_single_line(line)
                print_bars(line)
            if last_line is not None:
                print_single_line(last_line)
                print_bars(last_line)
