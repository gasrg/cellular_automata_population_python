"""This file is used to validate the model"""
import csv
import os

import matplotlib.pyplot as plt

from ..cellular_automata_population_python import Model


class Validator:
    def __init__(self):
        """Initiate the validator"""
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
                [float(a[1]) * 1000 for a in csv.reader(csv_file) if __test(a[1])]
                                   )[-self.model.max_steps - 2:-1]

    def plot_data_population(self):
        """Plot the data of the population from FRED"""
        plt.figure()
        plt.plot(self.data_population, "k--")
        plt.plot(self.model.population, "k-")
        plt.legend(["Data", "Model"])
        plt.xlabel("Step #")
        plt.ylabel("Population")
        plt.title("Comparision of Population Time Series for Data and Model")

    def print_errors(self):
        """Print Errors"""
        for t, (d, m) in enumerate(zip(self.data_population, self.model.population)):
            print("Step{}: data = {}, model = {}; error = {}".format(
                t,
                d,
                m,
                m - d,
            ))


if __name__ == "__main__":
    plt.style.use(["bmh", "grayscale"])
    validator = Validator()
    validator.print_errors()
    validator.plot_data_population()
    plt.show()
