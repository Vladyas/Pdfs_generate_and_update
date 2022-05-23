# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'probe_design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTreeView, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 645)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.listView)

        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.treeView)

        self.pushButtonListModel = QPushButton(self.centralwidget)
        self.pushButtonListModel.setObjectName(u"pushButtonListModel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pushButtonListModel)

        self.pushButtonTreeModel = QPushButton(self.centralwidget)
        self.pushButtonTreeModel.setObjectName(u"pushButtonTreeModel")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButtonTreeModel)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.listWidget)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.treeWidget)

        self.pushButtonListItem = QPushButton(self.centralwidget)
        self.pushButtonListItem.setObjectName(u"pushButtonListItem")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.pushButtonListItem)

        self.pushButtonTreeItemFill = QPushButton(self.centralwidget)
        self.pushButtonTreeItemFill.setObjectName(u"pushButtonTreeItemFill")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pushButtonTreeItemFill)

        self.pushButtonTreeItem = QPushButton(self.centralwidget)
        self.pushButtonTreeItem.setObjectName(u"pushButtonTreeItem")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pushButtonTreeItem)

        self.pushButtonGetFile = QPushButton(self.centralwidget)
        self.pushButtonGetFile.setObjectName(u"pushButtonGetFile")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pushButtonGetFile)

        self.pushButtonGetDir = QPushButton(self.centralwidget)
        self.pushButtonGetDir.setObjectName(u"pushButtonGetDir")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.pushButtonGetDir)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 633, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model based:", None))
        self.pushButtonListModel.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c Model List ", None))
        self.pushButtonTreeModel.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c Model Tree", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Item based:", None))
        self.pushButtonListItem.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c Item List ", None))
        self.pushButtonTreeItemFill.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c Item Tree", None))
        self.pushButtonTreeItem.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c Item Tree", None))
        self.pushButtonGetFile.setText(QCoreApplication.translate("MainWindow", u"getFile", None))
        self.pushButtonGetDir.setText(QCoreApplication.translate("MainWindow", u"getDir", None))
    # retranslateUi

