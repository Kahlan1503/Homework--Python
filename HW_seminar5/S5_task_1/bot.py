import random
class Bot:

    def __init__(self, difficult: int = 1):
        self.__difficult = difficult

    @staticmethod
    def easy(candies: int, max_candies: int) -> int:
        return random.randint(1, max_candies)

    @staticmethod
    def hard(candies: int, max_candies: int) -> int:
        better_move = candies % (max_candies + 1)
        if better_move == 0:
            return random.randint(1, max_candies)
        else:
            return candies % (max_candies + 1)

    @staticmethod
    def medium(candies: int, max_candies: int) -> int:
        if random.randint(0, 1):
            better_move = candies % (max_candies + 1)
            if better_move == 0:
                return random.randint(1, max_candies)
            else:
                return candies % (max_candies + 1)
        else:
            return random.randint(1, max_candies)

    def move(self, candies: int, max_candies: int) -> int:
        if self.__difficult == 1:
            return self.easy(candies, max_candies)
        if self.__difficult == 2:
            return self.medium(candies, max_candies)
        if self.__difficult == 3:
            return self.hard(candies, max_candies)