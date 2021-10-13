import sys
import random

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont


class GameWindow(QWidget):
    def __init__(
        self, parent=None, number=random.randint(1, 10), main_window: QWidget = None
    ):
        super().__init__(parent)

        self.main_window = main_window

        self.number = number

        self.setWindowTitle("Guess The Number")
        self.setFixedSize(300, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.title = QLabel("Guess The Number", self)
        self.title.setFont(QFont("Arial", 20))
        self.title.adjustSize()
        self.title.move(int(self.width() / 2 - self.title.width() / 2), 30)

        self.guess = QLabel("Guess", self)
        self.guess.setFont(QFont("Arial", 16))
        self.guess.adjustSize()
        self.guess.move(int(self.width() / 2 - self.guess.width() / 2), 80)

        self.guess_input = QLineEdit(self)
        self.guess_input.setFont(QFont("Arial", 16))
        self.guess_input.adjustSize()
        self.guess_input.setFixedWidth(150)
        self.guess_input.move(int(self.width() / 2 - self.guess_input.width() / 2), 110)
        self.guess_input.setReadOnly(True)

        self.one = QPushButton("1", self)
        self.one.setFont(QFont("Arial", 16))
        self.one.setFixedSize(30, 30)
        self.one.move(int(self.width() / 2 - self.one.width() / 2) - 30, 150)
        self.one.clicked.connect(self.one_clicked)

        self.two = QPushButton("2", self)
        self.two.setFont(QFont("Arial", 16))
        self.two.setFixedSize(30, 30)
        self.two.move(int(self.width() / 2 - self.two.width() / 2), 150)
        self.two.clicked.connect(self.two_clicked)

        self.three = QPushButton("3", self)
        self.three.setFont(QFont("Arial", 16))
        self.three.setFixedSize(30, 30)
        self.three.move(int(self.width() / 2 - self.three.width() / 2) + 30, 150)
        self.three.clicked.connect(self.three_clicked)

        self.four = QPushButton("4", self)
        self.four.setFont(QFont("Arial", 16))
        self.four.setFixedSize(30, 30)
        self.four.move(int(self.width() / 2 - self.four.width() / 2) - 30, 180)
        self.four.clicked.connect(self.four_clicked)

        self.five = QPushButton("5", self)
        self.five.setFont(QFont("Arial", 16))
        self.five.setFixedSize(30, 30)
        self.five.move(int(self.width() / 2 - self.five.width() / 2), 180)
        self.five.clicked.connect(self.five_clicked)

        self.six = QPushButton("6", self)
        self.six.setFont(QFont("Arial", 16))
        self.six.setFixedSize(30, 30)
        self.six.move(int(self.width() / 2 - self.six.width() / 2) + 30, 180)
        self.six.clicked.connect(self.six_clicked)

        self.seven = QPushButton("7", self)
        self.seven.setFont(QFont("Arial", 16))
        self.seven.setFixedSize(30, 30)
        self.seven.move(int(self.width() / 2 - self.seven.width() / 2) - 30, 210)
        self.seven.clicked.connect(self.seven_clicked)

        self.eight = QPushButton("8", self)
        self.eight.setFont(QFont("Arial", 16))
        self.eight.setFixedSize(30, 30)
        self.eight.move(int(self.width() / 2 - self.eight.width() / 2), 210)
        self.eight.clicked.connect(self.eight_clicked)

        self.nine = QPushButton("9", self)
        self.nine.setFont(QFont("Arial", 16))
        self.nine.setFixedSize(30, 30)
        self.nine.move(int(self.width() / 2 - self.nine.width() / 2) + 30, 210)
        self.nine.clicked.connect(self.nine_clicked)

        self.clear = QPushButton("CLEAR", self)
        self.clear.setFont(QFont("Arial", 10))
        self.clear.setFixedSize(60, 30)
        self.clear.move(int(self.width() / 2 - self.clear.width() / 2) - 15, 240)
        self.clear.clicked.connect(self.clear_clicked)

        self.zero = QPushButton("0", self)
        self.zero.setFont(QFont("Arial", 16))
        self.zero.setFixedSize(30, 30)
        self.zero.move(int(self.width() / 2 - self.zero.width() / 2) + 30, 240)
        self.zero.clicked.connect(self.zero_clicked)

        self.guess_hint = QLabel("You haven't guessed a number yet.", self)
        self.guess_hint.setFont(QFont("Arial", 9))
        self.guess_hint.adjustSize()
        self.guess_hint.move(int(self.width() / 2 - self.guess_hint.width() / 2), 285)

        self.guess_button = QPushButton("GUESS", self)
        self.guess_button.setFont(QFont("Arial", 16))
        self.guess_button.setFixedSize(150, 50)
        self.guess_button.move(
            int(self.width() / 2 - self.guess_button.width() / 2), 320
        )
        self.guess_button.clicked.connect(self.guess_button_clicked)

    def one_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "1")

    def two_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "2")

    def three_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "3")

    def four_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "4")

    def five_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "5")

    def six_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "6")

    def seven_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "7")

    def eight_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "8")

    def nine_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "9")

    def zero_clicked(self):
        self.guess_input.setText(self.guess_input.text() + "0")

    def clear_clicked(self):
        self.guess_input.setText("")

    def guess_correct(self):
        self.main_window.setFixedSize(250, 150)
        # move the main window to the center of this window
        self.main_window.move(
            self.x() + int(self.width() / 2 - self.main_window.width() / 2),
            self.y() + int(self.height() / 2 - self.main_window.height() / 2),
        )
        self.main_window.setVisible(True)
        self.close()

    def guess_button_clicked(self):
        if self.guess_input.text() == "":
            self.guess_hint.setText("You haven't guessed a number yet.")
        elif int(self.guess_input.text()) == self.number:
            self.guess_hint.setText("You guessed the number!")
            QTimer.singleShot(1000, self.guess_correct)
        elif int(self.guess_input.text()) > self.number:
            self.guess_hint.setText("Your guess is too high.")
        elif int(self.guess_input.text()) < self.number:
            self.guess_hint.setText("Your guess is too low.")
        self.guess_hint.adjustSize()
        self.guess_hint.move(int(self.width() / 2 - self.guess_hint.width() / 2), 285)
        self.guess_input.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = GameWindow()
    game.show()
    sys.exit(app.exec_())
