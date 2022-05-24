import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from get_google_data import get_creds
import design


def show_warning_box(large_text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.window().setWindowTitle('Предупреждение')
    msgBox.setText("Не установлены некоторые параметры...")
    msgBox.setInformativeText(large_text)
    msgBox.exec()


def login_google(window):
    window.gdata.creds = get_creds()

    return True if window.gdata.creds else False

def click_pattern_button():
    pass


def click_dir_button():
    pass


class MainWindow(QMainWindow, design.Ui_MainWindow):
    def __init__(self, dataobj):
        super().__init__()
        self.gdata = dataobj
        self.setupUi(self)
        self.loginButton.clicked.connect(self.click_login_button)
        self.patternButton.clicked.connect(click_pattern_button)
        self.dirButton.clicked.connect(click_dir_button)
        self.generateButton.clicked.connect(self.click_generate_button)

    def click_login_button(self):
        if not login_google(self):
            show_warning_box('Неудачная попытка логина в Google\n')

    def click_generate_button(self):
        # large_text = ''
        # large_text += 'Залогигились в Google Drive...'
        # gdata.creds = 1
        # gdata.spreadsheet_id = 1
        # gdata.sheet_name = 1
        # gdata.pdf_pattern_name = 1
        # gdata.pdf_field = 1
        # gdata.uniq_vals = 1
        # gdata.output_dir = 1
        #
        # if all([gdata.__getattribute__(x) for x in gdata.__dir__() if not x.startswith('__')]):
        #     print('Generation starts...')
        # else:
        show_warning_box('')
