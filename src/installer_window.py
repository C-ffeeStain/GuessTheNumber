"""Build and installs the program from GitHub."""


import os
from urllib.request import urlretrieve
from pathlib import Path

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
    QMessageBox,
    QCheckBox,
    QFileDialog,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from platformdirs import user_data_dir


def download_repo_file(
    filename: str,
    destination: str,
    author_name: str = "C-ffeeStain",
    repo_name: str = "GuessTheNumber",
):
    """Downloads a file from a GitHub repository and saves it to a file."""
    msg = urlretrieve(
        f"https://github.com/{author_name}/{repo_name}/raw/main/" + filename,
        Path(destination) / "install",
    )
    if msg[1] == "OK":
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")


class InstallerWindow(QMainWindow):
    """Builds and installs the program from GitHub."""

    author_name = "C-ffeeStain"
    repo_name = "GuessTheNumber"

    def __init__(self):
        """Initializes the window."""
        super().__init__()
        self.setWindowTitle("Installer")
        self.setFixedSize(300, 220)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.title = QLabel("Guess the Number: Installer", self)
        self.title.setFont(QFont("Arial", 16))
        self.title.adjustSize()
        self.title.move(int(self.width() / 2 - self.title.width() / 2), 10)

        self.install_folder_label = QLabel("Install Folder:", self)
        self.install_folder_label.setFont(QFont("Arial", 12))
        self.install_folder_label.adjustSize()
        self.install_folder_label.move(10, 50)

        self.install_folder_line_edit = QLineEdit(
            user_data_dir("GuessTheNumber", "C_ffeeStain"), self
        )
        self.install_folder_line_edit.setFixedWidth(175)
        self.install_folder_line_edit.setReadOnly(True)
        self.install_folder_line_edit.move(
            int(self.install_folder_label.x() + self.install_folder_label.width() + 5),
            45,
        )

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.adjustSize()
        self.browse_button.move(
            int(
                self.install_folder_line_edit.width() / 2
                - self.browse_button.width() / 2
            )
            + self.install_folder_line_edit.x(),
            self.install_folder_line_edit.y()
            + self.install_folder_line_edit.height()
            + 10,
        )
        self.browse_button.clicked.connect(self.browse_button_clicked)

        self.desktop_shortcut = QCheckBox("Create Desktop Shortcut", self)
        self.desktop_shortcut.setFont(QFont("Arial", 10))
        self.desktop_shortcut.adjustSize()
        self.desktop_shortcut.move(
            10,
            self.browse_button.y() + self.browse_button.height() + 10,
        )

        self.add_to_start_menu = QCheckBox("Add to Start Menu", self)
        self.add_to_start_menu.setFont(QFont("Arial", 10))
        self.add_to_start_menu.adjustSize()
        self.add_to_start_menu.move(
            10,
            self.desktop_shortcut.y() + self.desktop_shortcut.height() + 10,
        )

        self.install_button = QPushButton("Install", self)
        self.install_button.adjustSize()
        self.install_button.move(
            int(self.width() / 2 - self.install_button.width() / 2) - 60,
            self.add_to_start_menu.y() + self.add_to_start_menu.height() + 20,
        )
        self.install_button.clicked.connect(self.install_button_clicked)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.setFixedSize(
            self.install_button.width(), self.install_button.height()
        )
        self.cancel_button.move(
            int(self.width() / 2 - self.install_button.width() / 2) + 60,
            self.add_to_start_menu.y() + self.add_to_start_menu.height() + 20,
        )
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

    def browse_button_clicked(self):
        """Opens a file browser and sets the install folder."""
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select the install folder",
            self.install_folder_line_edit.text(),
        )
        if folder:
            self.install_folder_line_edit.setText(folder)

    def install_button_clicked(self):
        try:
            self.install()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred while installing the program.\n\n{e}",
            )

    def install(self):
        install_path = Path(self.install_folder_line_edit.text()) / "install"

        os.makedirs(install_path, exist_ok=True)
        os.chdir(self.install_folder_line_edit.text())

        os.system("attrib +h install")

        [
            download_repo_file("src/" + file, file)
            for file in ["game_window.py", "main_window.py", "main.py", "logger.py"]
        ]

        download_repo_file("icon.png", "icon.png")
        download_repo_file("VERSION", "VERSION")

        self.install_button.setEnabled(False)

        os.system(
            "pyinstaller --onefile --noconsole --icon icon.png --add-data VERSION;. --name GuessTheNumber  install/main.py"
        )

    def cancel_button_clicked(self):
        """Closes the window."""
        result = QMessageBox.question(
            self,
            "Cancel",
            "Are you sure you want to cancel the installation?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if result == QMessageBox.Yes:
            self.close()


def main():
    """Runs the program."""
    app = QApplication([])
    window = InstallerWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
