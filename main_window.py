import sys

import PyPDF2
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow,
                               QMessageBox, QTreeWidgetItem, QFileDialog, QListWidgetItem)
from get_google_data import get_creds, get_spreadsheets, get_sheet_range, get_treeWidget_dict
from PyPDF2 import PdfFileReader, PdfFileWriter

import design
from generate_pdfs import generate_pdfs
from config import *

class QTreeWidgetItem_withId(QTreeWidgetItem):
    def __init__(self, l, id):
        super(QTreeWidgetItem_withId, self).__init__(l)
        self.id = id


class PdfFiledsItem(QListWidgetItem):
    def __init__(self, pdf_alt_name, pdf_field_name):
        super().__init__(pdf_alt_name)
        self.name = pdf_field_name


def show_warning_box(short_text, long_text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.window().setWindowTitle('Предупреждение')
    msgBox.setText(short_text)
    msgBox.setInformativeText(long_text)
    msgBox.exec()


def login_google(window):
    window.gdata.creds = get_creds()
    if window.gdata.creds:
        window.initTreeWidget()
    return True if window.gdata.creds else False


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
        self.patternButton.clicked.connect(self.click_pattern_button)
        self.dirButton.clicked.connect(self.click_dir_button)
        self.generateButton.clicked.connect(self.click_generate_button)

        self.treeWidget.expanded.connect(self.enpanded_treeWidged)

    def initTreeWidget(self):
        items = []

        # clear treeWidget
        while (self.treeWidget.topLevelItemCount() > 0):
            self.treeWidget.takeTopLevelItem(0)

        for d in get_treeWidget_dict(self.gdata.creds, get_spreadsheets(self.gdata.creds)):
            item = QTreeWidgetItem_withId([d['name'], d['sheet1'], d['owner']], d['id'])
            for sheet in d['sheets'][1:]:
                child = QTreeWidgetItem_withId(['', sheet, ''], d['id'])
                item.addChild(child)
            items.append(item)

        self.treeWidget.insertTopLevelItems(0, items)
        # for i in get_spreadsheets(get_creds()):

    def enpanded_treeWidged(self):
        pass

    def click_login_button(self):
        if not login_google(self):
            show_warning_box('Неудачная попытка логина в Google', '')

    def _generate_check(self):
        error_text = ''
        if not self.gdata.creds:
            error_text += "Вы не залогинены\n"
        elif not self.treeWidget.currentItem():
            error_text += "Выберите лист в Google таблице\n"

        if not self.pdfPattern.text():
            error_text += "Выберите PDF шаблон\n"
        if not self.listWidgetPdfFields.selectedItems():
            error_text += "Выберите PDF поле для заполнения\n"
        elif not self.copyNumber.text():
            error_text += "Выберите количество генерируемых файлов\n"

        if not self.outputDir.text():
            error_text += "Выберите директорию для генерации PDF файлов\n"

        if error_text:
            show_warning_box('Не выбранны все данные для генерации!', error_text)
            return False

        return True

    def click_generate_button(self):
        if self._generate_check():
            self.gdata.spreadsheet_id = self.treeWidget.currentItem().id
            self.gdata.range = self.treeWidget.currentItem().text(1) + RANGE
            self.gdata.pdf_pattern_name = self.pdfPattern.text()
            self.gdata.pdf_field = self.listWidgetPdfFields.currentItem().name
            self.gdata.files_amount = int(self.copyNumber.text())
            self.gdata.output_dir = self.outputDir.text()

            generated, msg = generate_pdfs(self.gdata, self.progressBar)
            if not generated:
                show_warning_box('Ошибка генерации', msg)
            else:
                print(msg)
    def click_pattern_button(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("PDF files (*.pdf)")
        dialog.setViewMode(QFileDialog.Detail)
        fileNames = ''

        if dialog.exec():
            fileNames = dialog.selectedFiles()[0]

        if fileNames:
            self.pdfPattern.setText(fileNames)

            reader = PdfFileReader(fileNames)
            fields = reader.get_fields()
            self.listWidgetPdfFields.clear()
            for i in fields.values():
                if i.fieldType == '/Tx':
                    self.listWidgetPdfFields.addItem(
                        PdfFiledsItem(f'{i.name} (алтернативное имя: {i.altName} )', i.name))

    def click_dir_button(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        # dialog.setViewMode(QFileDialog.Detail)
        dirName = ''
        # fileNames = QStringList()
        if dialog.exec():
            dirName = dialog.selectedFiles()
        if dirName:
            self.outputDir.setText(dirName[0])
            pass
