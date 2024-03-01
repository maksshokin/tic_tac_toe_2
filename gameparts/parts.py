class Board:
    """Класс, который описывает игровое поле."""

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        """Функция, делающая ход."""
        self.board[row][col] = player

    def display(self):
        """Вывод дисплея."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5) 