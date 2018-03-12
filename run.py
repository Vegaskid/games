import probabilitygames as pg

# The auto_run() method is useful for collecting stats on a fixed number of games. For this purpose, it doesn't make
# sense for the number of doors to change per game in each run, however, the player door is randomly selected for a more
# realistic simulation

# Create a game instance for a 10 door game
game = pg.Monty(10)
# Run the simulation 1000 times
game.auto_run(1000)
