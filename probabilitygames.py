import random
import os


class Monty:
    """
        Representation of the Monty Hall probability problem.
    """

    def __init__(self, num_of_doors=3, player_door=1):
        """
        :param num_of_doors: must be >= 3
        :param player_door: must be a door that can exist based on tnum_of_doors
        """
        self.num_of_doors = num_of_doors
        self.player_door = player_door
        self._build_doors()
        self.doors_start = []
        self.doors_end = []
        self.doors_temp = []

    def _pre_checks(self):
        """
        Checks values before continuing to make sure they are valid or clears them as relevant.
        """
        if self.num_of_doors < 3:
            print("Not enough doors to play with. Setting game with 3 doors")
            self.num_of_doors = 3
        if self.player_door - 1 not in range(self.num_of_doors):
            print("You have selected a door that doesn't exist. Door 1 now selected.")
            self.player_door = 1
        self.doors_start = []
        self.doors_end = []
        self.doors_temp = []

    def _build_doors(self):
        """
        The self.doors_start list represents the random door selection of length self.num_of_doors before anything
        has been opened with the following key:
            G = door with goat
            C = door with car
        """
        self._pre_checks()
        for i in range(self.num_of_doors):
            self.doors_start.append("G")
        self.doors_start[random.randint(0, self.num_of_doors - 1)] = "C"

    def choose_door(self):
        """
        Asks for a manual player door choice until that choice is a door that exists.
        """
        while True:
            os.system('cls')
            player_door = input("Please let me know which door you want to pick (1-{})".format(self.num_of_doors))
            try:
                if int(player_door) in range(self.num_of_doors):
                    self.player_door = player_door
                    break
            except ValueError:
                print("You must enter a number between 1 and {}".format(self.num_of_doors))

    def open_doors(self):
        """
        This method simulates the opening of all but one of the non-player doors as per the rules of the game.
        That leaves us with two doors:
            The player's selected door
            The last unopened door that Monty leaves
        All other doors are ones with goats that Monty has opened. A new list is created that contains just those two
        doors, the user door always at index 0 and the last unopened door at index 1. This allows us to run the
        simulation in a consistent manner.

        A copy of the self.doors_start is used. This leaves the original doors untouched for comparison.
        and pop the player door and the remaining goats until there is only one door left.

        Note that self.player_door - 1 is used here because the doors are numbered from 1 but the door list is
        zero based
        """
        self.doors_end = []
        self.doors_temp = list(self.doors_start)
        self.doors_end.append(self.doors_start[self.player_door - 1])
        self.doors_temp.pop(self.player_door - 1)

        while len(self.doors_temp) != 1:
            random_door = random.randint(0, len(self.doors_temp) - 1)
            if self.doors_temp[random_door] == "G":
                self.doors_temp.pop(random_door)
        self.doors_end.append(self.doors_temp[0])

    def reset(self):
        self.__init__()

    def auto_run(self, number_of_runs=1):
        """
        :param number_of_runs: how many times to run the simulation

        Each run picks a new player door, builds a new random door list and opens them as per the game rules.
        Each run has the game number, starting doors, player door and the last two doors printed out.
        Once all runs have completed, summary statistics are printed.
        This provides a way to validate each run of the game to ensure no cheating is going on.
        """
        count = 0
        for i in range(number_of_runs):
            self.player_door = random.randint(1, self.num_of_doors)
            self._build_doors()
            self.open_doors()
            print("===========================================================")
            print("Game number: {}".format(i + 1))
            print("Doors at the start of the game: {}".format(self.doors_start))
            print("Player door: {}".format(self.player_door))
            print("Last two doors, the player door, then the last unopened door: {}".format(self.doors_end))
            if self.doors_end[0] == "G":
                count += 1

        print("===========================================================\n")
        print("Number of times you picked a goat and therefore a switch would win you the car: {}".format(count))
        print("Number of times you picked the car and therefore" +
              "a switch would win you a goat: {}".format(number_of_runs - count))
        print("\nProbability of winning the car due to a switch: {}".format(count / number_of_runs))
        print(
            "Probability of winning the car due to a switch, as a percentage: {}%".format(count / number_of_runs * 100))
