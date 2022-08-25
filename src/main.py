import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from main_window import MainWindow
from data_classes import GData

def main():
    app = QApplication([])
    gdata = GData()
    window = MainWindow(gdata)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
