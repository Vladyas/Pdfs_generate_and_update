import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

import design


def show_warning_box():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.window().setWindowTitle('Предупреждение')
    msgBox.setText("Не установлены некоторые параметры...")
    msgBox.setInformativeText("Больше информационного текста")
    msgBox.exec()


def click_login_button():
    pass


def click_pattern_button():
    pass


def click_dir_button():
    pass


def click_generate_button():
    show_warning_box()


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.loginButton.clicked.connect(click_login_button)
        self.patternButton.clicked.connect(click_pattern_button)
        self.dirButton.clicked.connect(click_dir_button)
        self.generateButton.clicked.connect(click_generate_button)
