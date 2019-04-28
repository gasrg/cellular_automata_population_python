import csv
import os

import matplotlib.pyplot as plt

import Model


class Validator():
    def __init__(self):
        self.model = Model.Model()
        self.model.run()

        def __test(t):
            try:
                float(t)
                return True
            except ValueError:
                return False

        with open(os.path.join("Data", "POPTHM.csv")) as csv_file:
            self.data_population = (
                                       [float(a[1]) for a in csv.reader(csv_file) if __test(a[1])]
                                   )[-self.model.max_steps - 2:-1]

        self.multiplier = self.data_population[0] / self.model.count_alive[0]

    def plot_data_population(self):
        plt.figure()
        plt.plot(self.data_population, "k--")
        plt.plot([a * self.multiplier for a in self.model.count_alive], "k-")
        plt.legend(["Data", "Model"])
        plt.xlabel("Step #")
        plt.ylabel("Population")
        plt.title("Comparision of Population Time Series for Data and Model")
        plt.figure()
        plt.plot(self.data_population, [a * self.multiplier for a in self.model.count_alive], "k-")
        plt.xlabel("Data")
        plt.ylabel("Model")
        plt.title("Population from Model vs. Population from Data")
        plt.show()

    def print_errors(self):
        for t, (d, m) in enumerate(zip(self.data_population, self.model.count_alive)):
            print("Step{}: data = {}, model * multiplier = {}; error = {}".format(
                t,
                d,
                m * self.multiplier,
                m * self.multiplier - d,
            ))


if __name__ == "__main__":
    plt.style.use(["bmh", "grayscale"])
    validator = Validator()
    validator.print_errors()
    validator.plot_data_population()
