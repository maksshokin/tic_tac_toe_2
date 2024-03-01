from gameparts import Board

def main():
    """Функция, выводящая данные."""
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display()

print(print.__doc__)

if __name__ == '__main__':
    main() 