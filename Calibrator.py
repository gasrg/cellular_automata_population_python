import csv
import os
import random

import matplotlib.pyplot as plt

import Model


class Calibrator:
    def __init__(self):
        print("Creating the model...")
        self.model = Model.Model()
        self.model.run()
        self.history_a = []
        self.history_b = []
        self.history_lowest_error = []

        def __test(t):
            try:
                float(t)
                return True
            except ValueError:
                return False

        print("Reading the Data file...")
        with open(os.path.join("Data", "POPTHM.csv")) as csv_file:
            self.data_population = (
                [float(a[1]) * 1000 for a in csv.reader(csv_file) if __test(a[1])]
                        )[-self.model.max_steps - 2:-1]
        print("Starting opt...")
        guess_a = 200000
        guess_b = 9
        best_a = guess_a
        best_b = guess_b
        lowest_error = 0.0
        for step in [5, 1, 0.5, 0.25, 0.1]:
            print("Step = {}".format(step))
            no_move_count = 0
            while no_move_count < 200:
                guess_a = best_a
                guess_b = best_b
                if random.choice([True, False]):
                    guess_a += random.choice([-step, step])
                else:
                    guess_b += random.choice([-step, step])
                population = [
                    1000 * (guess_a + guess_b * p) for p in self.model.count_alive]
                error = sum(
                    (m - d) ** 2 for m, d in zip(population, self.data_population)
                )
                if error < lowest_error or lowest_error == 0:
                    lowest_error = error
                    best_a = guess_a
                    best_b = guess_b
                    no_move_count = 0
                    self.history_a.append(best_a)
                    self.history_b.append(best_b)
                    self.history_lowest_error.append(lowest_error)
                    print("error = {}: Population = {} + {} * count_alive".format(
                        error,
                        best_a,
                        best_b
                    ))
                else:
                    no_move_count += 1
        print("Done!")

    def plot_errors(self):
        plt.cla()
        plt.subplot(311)
        plt.plot(self.history_a)
        plt.ylabel("a")
        plt.subplot(312)
        plt.plot(self.history_b)
        plt.ylabel("b")
        plt.subplot(313)
        plt.plot(self.history_lowest_error)
        plt.ylabel("Error")


if __name__ == "__main__":
    c = Calibrator()
    c.plot_errors()
    plt.show()
