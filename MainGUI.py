import logging

import easygui
import matplotlib.pyplot as plt

import Calibrator
import Model
import Validator


class MainGUI:
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)

    def ask(self):
        choices = [
            "Run Model",
            "Run Validation",
            "Run Calibration"
        ]
        ans = easygui.buttonbox(
            "Choose an option to run",
            "Cellular Automata Popular Model",
            choices
        )
        if ans == choices[0]:
            self.run_model()
        elif ans == choices[1]:
            self.run_validation()
        elif ans == choices[2]:
            self.run_calibrator()

    def run_model(self):
        plt.rcParams["figure.figsize"] = [5, 6]
        ca = Model.Model()
        ca.run(plot=True)

    def run_validation(self):
        validator = Validator.Validator()
        validator.print_errors()
        validator.plot_data_population()
        plt.show()

    def run_calibrator(self):
        c = Calibrator.Calibrator()
        c.plot_errors()
        plt.show()


if __name__ == "__main__":
    gui = MainGUI()
    gui.ask()
