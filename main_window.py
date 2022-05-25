import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QTreeWidgetItem
from get_google_data import get_creds, get_spreadsheets, get_sheet_range, get_treeWidget_dict
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
    if window.gdata.creds:
        window.initTreeWidget()
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

        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(["Таблица", "Лист", "Владелец"])

        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(["Таблица", "Лист", "Владелец"])
        self.loginButton.clicked.connect(self.click_login_button)
        self.patternButton.clicked.connect(click_pattern_button)
        self.dirButton.clicked.connect(click_dir_button)
        self.generateButton.clicked.connect(self.click_generate_button)

        self.treeWidget.expanded.connect(self.enpanded_treeWidged)

    def initTreeWidget(self):
        items = []

        # clear treeWidget
        while (self.treeWidget.topLevelItemCount() > 0):
            self.treeWidget.takeTopLevelItem(0)

        for d in get_treeWidget_dict(self.gdata.creds, get_spreadsheets(self.gdata.creds)):
            item = QTreeWidgetItem([d['name'], d['sheet1'], d['owner']])
            for sheet in d['sheets'][1:]:
                child = QTreeWidgetItem(['', sheet, ''])
                item.addChild(child)
            items.append(item)

        self.treeWidget.insertTopLevelItems(0, items)
        # for i in get_spreadsheets(get_creds()):

    def enpanded_treeWidged(self):
        pass

    def click_login_button(self):
        if not login_google(self):
            show_warning_box('Неудачная попытка логина в Google\n')

    def click_generate_button(self):
        show_warning_box('')
