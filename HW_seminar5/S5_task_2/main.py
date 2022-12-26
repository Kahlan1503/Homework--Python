from game import Game


def print_board(board: list):
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[0]} | {board[1]} | {board[2]} ')


def enter_numb() -> int:
    while True:
        number = input('Enter a number between 1 and 9. \n').lower()
        if number == 'help':
            print_board([i for i in '123456789'])
            continue
        if number.isdigit() and int(number) > 0 and len(number) == 1:
            if game.board[int(number) - 1] == " ":
                return int(number)
            else:
                print("Cell isn't empty!")


def x_or_o() -> str:
    while (n := 0) <= 5:
        n += 1
        print('Do you want play by X or O')
        if (symb := input().lower()) == 'x' or n > 5:
            return 'X'
        elif symb == 'o':
            return 'O'


def y_n() -> bool:
    while True:
        answer = input('(Y/N)?').lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        print('Incorrect input.')


while True:
    game = Game()
    game.first_move(x_or_o())
    game.start_game()

    while game.game_status == 'IN_PROGRESS':
        print_board(game.board)
        print(f'Move {game.turn}')
        game.move(enter_numb())
    print_board(game.board)

    if game.game_status == 'X_WON':
        print('X won!')
    elif game.game_status == 'O_WON':
        print('O won!')
    elif game.game_status == 'TIE':
        print('Appears to be a tie')

    print('Do yow want play more?')
    if not y_n():
        break
