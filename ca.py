import random
import time
import sys
import os

random.seed(2)


class CellularAutomata:
    def __init__(self):
        self.step = 0
        self.max_steps = 1000
        self.sleep_time = 0.1  # Time to sleep between steps, in secs.
        self.height = 40
        self.width = 120
        self.p_dying = 0.1  # probability of dying
        self.p_birth = 0.08  # Probability of getting born
        self.p_starving = 0.2  # Probability of getting born
        self.total_number_alive = 0
        self.cells = [[1 if random.random() >= 0.9 else 0 for i in range(self.width)] for ii in range(self.height)]

    def do_step(self):
        self.step += 1
        self.total_number_alive = 0
        for r in range(self.height):
            for c in range(self.width):
                number_of_neighbors = (self.cells[r-1][c] +
                                       self.cells[r+1 if r+1 < self.height else 0][c] +
                                       self.cells[r][c-1] +
                                       self.cells[r][c+1 if c+1 < self.width else 0] +
                                       self.cells[r-1][c-1] +
                                       self.cells[r+1 if r+1 < self.height else 0][c+1 if c+1 < self.width else 0] +
                                       self.cells[r+1 if r+1 < self.height else 0][c-1] +
                                       self.cells[r-1][c+1 if c+1 < self.width else 0])

                # Some die with time
                if self.cells[r][c] == 1:
                    self.cells[r][c] = 0 if random.random() > (1 - self.p_dying) else 1

                # Some starve
                if self.cells[r][c] == 1 and number_of_neighbors >= 5:
                    self.cells[r][c] = 0 if random.random() > (1 - self.p_starving) else 1

                # Some are born
                if self.cells[r][c] == 0 and number_of_neighbors >= 2:
                    self.cells[r][c] = 1 if random.random() > (1-self.p_birth) else 0

                if self.cells[r][c] == 1:
                    self.total_number_alive += 1

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        output = ""
        output += "Step: " + str(self.step) + "; "
        output += "Total Alive: " + str(self.total_number_alive) + "\n"
        for row in self.cells:
            output += "".join(['X' if i == 1 else ' ' if i == 0 else "!" for i in row]) + "\n"
        sys.stdout.write(output)
        sys.stdout.flush()



    def run(self):
        self.print_grid()
        while self.step <= self.max_steps:
            self.do_step()
            self.print_grid()
            time.sleep(self.sleep_time)


ca = CellularAutomata()
ca.run()
