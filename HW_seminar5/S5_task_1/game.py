import random


class Game:

    def __init__(self, candies: int = None, max_candies: int = 28):
        self.__candies = random.randint(50, 2000) if candies is None else candies
        self.__turn = 0
        self.__max_candies = max_candies
        self.__game_status = 1

    def take_sweets(self, numb: int) -> None:
        if self.__game_status:
            self.__candies -= numb
            self.__change_turn()
        self.check_game()

    def __change_turn(self) -> None:
        if self.__turn == 0:
            self.__turn = 1
        else:
            self.__turn = 0

    def check_game(self) -> None:
        if self.__candies < 1:
            self.__game_status = 0
            self.__candies = 0
            self.__change_turn()

    @property
    def game_status(self) -> int:
        return self.__game_status

    @property
    def max_candies(self) -> int:
        return self.__max_candies

    @property
    def candies(self) -> int:
        return self.__candies

    @property
    def turn(self) -> int:
        return self.__turn