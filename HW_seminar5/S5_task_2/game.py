class Game:

    def __init__(self):
        self.__board = [' '] * 9
        self.__turn = 'X'
        self.__game_status = 'NOT_STARTED'

    def move(self, numb: int):
        if self.__game_status == 'IN_PROGRESS':
            if self.__board[numb - 1] == ' ':
                if self.__turn == 'X':
                    self.__board[numb - 1] = self.__turn
                elif self.__turn == 'O':
                    self.__board[numb - 1] = self.__turn
                self.__check_win(numb - 1)
                self.__change_turn()
            else:
                raise ValueError('You can only go to an empty cell')
        else:
            raise RuntimeError("GameOver")

    def start_game(self):
        if self.__game_status == 'NOT_STARTED':
            self.__game_status = 'IN_PROGRESS'
        else:
            raise RuntimeError("The game has already started")

    def __change_turn(self):
        if self.__turn == 'X':
            self.__turn = 'O'
        else:
            self.__turn = 'X'

    def first_move(self, symbol: str) -> str:
        if self.__game_status != 'NOT_STARTED':
            raise RuntimeError("You can't change your turn during the game")
        if symbol.lower() == 'x':
            self.__turn = 'X'
            return 'X'
        elif symbol.lower() == 'o':
            self.__turn = 'O'
            return 'O'
        else:
            raise ValueError('Only X or O')

    def __check_win(self, numb: int):
        range_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(len(range_win)):
            if numb in range_win[i]:
                win = set()
                for j in range_win[i]:
                    win.add(self.__board[j])
                if len(win) == 1:
                    if self.__turn == 'X':
                        self.__game_status = 'X_WON'
                    else:
                        self.__game_status = 'O_WON'
        if self.__game_status == 'IN_PROGRESS' and ' ' not in self.__board:
            self.__game_status = 'TIE'

    @property
    def board(self) -> list:
        return self.__board

    @property
    def game_status(self) -> str:
        return self.__game_status

    @property
    def turn(self) -> str:
        return self.__turn