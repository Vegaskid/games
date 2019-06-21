from random import randint


class Bingo:

    def __init__(self):
        self.numbers_called = []

    def _new_game(self):
        self.numbers_called = []

    def _generate_number(self):
        valid_number = -1
        while valid_number == -1:
            called_number = randint(1, 100)
            if called_number not in self.numbers_called:
                self.numbers_called.append(called_number)
                valid_number = 1

    def _create_all_numbers(self):
        self._new_game()
        for i in range(100):
            self._generate_number()
            print(len(self.numbers_called))

    def play(self):
        self._new_game()
        self._create_all_numbers()
