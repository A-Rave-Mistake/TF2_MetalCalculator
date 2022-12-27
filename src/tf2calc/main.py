#!/usr/bin/env python3

from GUI import MainWindow
from currency import CurrencyContainer


# ----- Script Activates ----- #
if __name__ == "__main__":
    total_currency = CurrencyContainer()
    MainWindow = MainWindow(total_currency)