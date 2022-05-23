import sys

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow,
                               QMessageBox, QTreeWidgetItem, QFileDialog)
import probe_design


def prepare_tree_items():
    data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
            "Project B": ["file_b.csv", "photo.jpg"],
            "Project C": []}
    items = []
    for key, values in data.items():
        item = QTreeWidgetItem([key])
        for value in values:
            ext = value.split(".")[-1].upper()
            child = QTreeWidgetItem([value, ext])
            item.addChild(child)
        items.append(item)
    return items


class MainWindow(QMainWindow, probe_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButtonTreeItemFill.clicked.connect(self._initTreeWidget)
        self.pushButtonTreeItem.clicked.connect(self._clearTreeWidget)
        self.pushButtonGetFile.clicked.connect(self._getfile)

    def _initTreeWidget(self):
        self.treeWidget.insertTopLevelItems(0, prepare_tree_items())

    def _clearTreeWidget(self):
        while (self.treeWidget.topLevelItemCount() > 0):
            self.treeWidget.takeTopLevelItem(0)

    def _getfile(self):
        QFileDialog.FileMode = QFileDialog.ExistingFile
        fileName = QFileDialog.getOpenFileName(self,
                                               "Выберите PDF образец с полями ввода", "", "PDF Files (*.pdf)")
        print(fileName)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
