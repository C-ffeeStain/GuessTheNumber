import sys
import os

from PyQt5.QtWidgets import QApplication

from logger import Logger
from main_window import MainWindow


def check_version():
    if not getattr(sys, "frozen", False):
        with open("VERSION") as f:
            version = f.read().strip().split(";")[0]
    else:
        with open(os.path.join(sys._MEIPASS, "VERSION")) as f:
            version = f.read().strip().split(";")[0]
    return version


def main():
    Logger("guessthenumber").info(f"Starting Guess the Number v{check_version()}...")
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
