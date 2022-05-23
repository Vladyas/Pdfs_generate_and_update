import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from main_window import MainWindow





def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
