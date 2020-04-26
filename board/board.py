import sys

class Board(object):

    def __init__(self, w=5, h=5):
        self._w = w
        self._h = h
        self.set_start(0, 0)
        self.set_end(self._w - 1, self._h - 1)
    
    def set_start(self, i, j):
        self._check_within_bound(i, j)
        self._board = [[False for _ in range(self._h)] for _ in range(self._w)]
        self._start = (i, j)
        self._current = self._start
        self._place_marker()
    
    def _place_marker(self):
        i, j = self._current
        self._board[i][j] = True

    def set_end(self, i, j):
        self._check_within_bound(i, j)
        self._end = (i, j)

    def _check_within_bound(self, x, y):
        if x < 0 or x >= self._w or y < 0 or y >= self._h:
            raise Exception('The position is not valid')

    def move_up(self):
        self._move(-1, 0)

    def move_down(self):
        self._move(1, 0)

    def move_left(self):
        self._move(0, -1)

    def move_right(self):
        self._move(0, 1)

    def _move(self, dx, dy):
        x, y = self._current
        new_x, new_y = x + dx, y + dy
        self._check_within_bound(new_x, new_y)
        self._current = (new_x, new_y)
        self._place_marker()
        self.print()

    def print(self):
        print(f'Current position: {self._current}. start: {self._start}, end: {self._end}. The board size: {self._w}x{self._h}')
        if self._current == self._end:
            print('YOU HAVE REACHED YOUR DESTINATION!')
        for i in range(self._w):
            print(''.join(['-'] * (4 * self._w + 1)))
            rows = ['|']
            for j in range(self._h):
                val = ' x ' if self._board[i][j] else '   '
                val = ' S ' if (i, j) == self._start else val
                val = ' E ' if (i, j) == self._end else val
                rows.append(f'{val}|')
            print(''.join(rows))
        print(''.join(['-'] * (4 * self._w + 1)))
            
