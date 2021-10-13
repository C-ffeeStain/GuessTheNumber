"""Main Window of the Guess the Number game written using PyQt5."""


import random
import logging

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from game_window import GameWindow
from logger import Logger


class MainWindow(QMainWindow):
    """Main window of the game."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()

        self.logger = Logger("guessthenumber")

        self.logger.info("Starting the main menu...")

        # Set the title of the window
        self.setWindowTitle("Guess the Number")

        # make the window borderless
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set the size of the window
        self.setFixedSize(250, 150)

        # Create the label for the game
        self.label = QLabel("Guess the Number", self)
        self.label.setFont(QFont("Arial", 14))
        self.label.adjustSize()
        self.label.move(int(self.width() / 2 - self.label.width() / 2), 10)

        # Create the button to start the game
        self.start_button = QPushButton("Start", self)
        self.start_button.setFont(QFont("Arial", 12))
        self.start_button.adjustSize()
        self.start_button.setFixedWidth(175)
        self.start_button.move(
            int(self.width() / 2 - self.start_button.width() / 2),
            self.label.y() + self.label.height() + 20,
        )
        self.start_button.setDefault(True)
        self.start_button.clicked.connect(self.start_game)

        # Create the button to quit the game
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setFont(QFont("Arial", 12))
        self.quit_button.adjustSize()
        self.quit_button.setFixedWidth(175)
        self.quit_button.move(
            int(self.width() / 2 - self.quit_button.width() / 2),
            self.start_button.y() + self.start_button.height() + 20,
        )
        self.quit_button.clicked.connect(self.quit_game)

        self.logger.info("Main menu started successfully.")

    def start_game(self):
        self.logger.info("Starting the game window...")
        try:
            self.game = GameWindow(main_window=self)
            self.game.show()
        except Exception as e:
            self.logger.error(f"Error while starting the game window: {e}")
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred while starting the game window: {e}... Please submit this to the discord for help.",
            )
        self.setFixedSize(1, 1)
        self.move(0, 0)
        self.setVisible(False)

    def quit(self):
        self.logger.info("Quitting the game...")
        self.close()

    def quit_game(self):
        """Quit the game."""
        response = QMessageBox.question(
            self,
            "Quit",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if response == QMessageBox.Yes:
            QApplication.quit()


if __name__ == "__main__":
    # Create the application
    app = QApplication([])

    # Create the main window
    main_window = MainWindow()

    # Show the main window
    main_window.show()

    # Execute the application
    app.exec_()
