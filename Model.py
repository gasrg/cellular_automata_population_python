import logging
import random
import time

import matplotlib.pyplot as plt
import numpy as np

random.seed(2)


class CellularAutomata:
    def __init__(self):
        self.step = 0
        self.max_steps = 1000
        self.sleep_time = 0.01  # Time to sleep between steps, in secs.
        self.height = 100
        self.width = 100
        self.p_dying = 0.1  # probability of dying
        self.p_birth = 0.08  # Probability of getting born
        self.p_starving = 0.2  # Probability of getting born
        self.total_number_alive = 0
        self.cells = np.array(
            [[1 if random.random() >= 0.9 else 0 for i in range(self.width)] for ii in range(self.height)]
        )
        self.count_alive = [np.count_nonzero(self.cells), ]

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
        # Re-count the cells alive
        self.count_alive.append(np.count_nonzero(self.cells))

    def run(self, plot=False):
        if plot:
            plt.ion()
        while self.step <= self.max_steps:
            self.do_step()
            if plot:
                plt.cla()
                plt.subplot(211)
                plt.imshow(self.cells)
                plt.title("Cells")
                plt.subplot(212)
                plt.plot(self.count_alive)
                plt.ylabel("# Cells Alive")
                plt.xlabel("Step #")
                plt.pause(0.001)
            logging.info("Alive = {} ({}%)".format(
                self.count_alive[-1],
                round(self.count_alive[-1] / self.width / self.height * 100, 0)
            ))
            time.sleep(self.sleep_time)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    plt.rcParams["figure.figsize"] = [5, 7]
    ca = CellularAutomata()
    ca.run(plot=True)
