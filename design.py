# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 580)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 360))
        MainWindow.setMaximumSize(QSize(1908, 1080))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(False)
        self.actionLogin = QAction(MainWindow)
        self.actionLogin.setObjectName(u"actionLogin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loginButton = QPushButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.loginButton)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy2)
        self.loginButton.setMaximumSize(QSize(261, 16777215))
        self.loginButton.setSizeIncrement(QSize(0, 0))
        self.loginButton.setBaseSize(QSize(800, 30))
        self.loginButton.setFont(font)
        self.loginButton.setContextMenuPolicy(Qt.CustomContextMenu)
        self.loginButton.setAcceptDrops(False)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setCheckable(False)
        self.loginButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.loginButton)

        self.label_treeWidget = QLabel(self.centralwidget)
        self.label_treeWidget.setObjectName(u"label_treeWidget")
        self.label_treeWidget.setFont(font)

        self.verticalLayout.addWidget(self.label_treeWidget)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        self.treeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setMinimumSectionSize(100)
        self.treeWidget.header().setDefaultSectionSize(400)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setProperty("showSortIndicator", True)
        self.treeWidget.header().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.treeWidget)

        self.patternButton = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.patternButton)
        self.patternButton.setObjectName(u"patternButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.patternButton.sizePolicy().hasHeightForWidth())
        self.patternButton.setSizePolicy(sizePolicy3)
        self.patternButton.setMaximumSize(QSize(261, 16777215))
        self.patternButton.setFont(font)
        self.patternButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.patternButton)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.lineEdit)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.label_copyNumber = QLabel(self.centralwidget)
        self.label_copyNumber.setObjectName(u"label_copyNumber")
        self.label_copyNumber.setEnabled(True)
        self.label_copyNumber.setFont(font)

        self.verticalLayout.addWidget(self.label_copyNumber)

        self.copyNumber = QLineEdit(self.centralwidget)
        self.copyNumber.setObjectName(u"copyNumber")
        sizePolicy2.setHeightForWidth(self.copyNumber.sizePolicy().hasHeightForWidth())
        self.copyNumber.setSizePolicy(sizePolicy2)
        self.copyNumber.setBaseSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.copyNumber)

        self.dirButton = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.dirButton)
        self.dirButton.setObjectName(u"dirButton")
        sizePolicy2.setHeightForWidth(self.dirButton.sizePolicy().hasHeightForWidth())
        self.dirButton.setSizePolicy(sizePolicy2)
        self.dirButton.setMaximumSize(QSize(261, 16777215))
        self.dirButton.setFont(font)
        self.dirButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.dirButton)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.generateButton = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.generateButton)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy3)
        self.generateButton.setMaximumSize(QSize(261, 16777215))
        self.generateButton.setFont(font)
        self.generateButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.generateButton)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.closeButton = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.closeButton)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy2.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy2)
        self.closeButton.setFont(font)
        self.closeButton.setFocusPolicy(Qt.TabFocus)
        self.closeButton.setLayoutDirection(Qt.RightToLeft)
        self.closeButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.closeButton)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.loginButton, self.treeWidget)
        QWidget.setTabOrder(self.treeWidget, self.patternButton)
        QWidget.setTabOrder(self.patternButton, self.listView)
        QWidget.setTabOrder(self.listView, self.copyNumber)
        QWidget.setTabOrder(self.copyNumber, self.dirButton)
        QWidget.setTabOrder(self.dirButton, self.generateButton)
        QWidget.setTabOrder(self.generateButton, self.closeButton)

        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close)

        self.loginButton.setDefault(True)
        self.patternButton.setDefault(False)
        self.dirButton.setDefault(False)
        self.generateButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 PDF \u0444\u0430\u0439\u043b\u043e\u0432 \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443", None))
        self.actionLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(tooltip)
        self.actionLogin.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043b\u043e\u0433\u0438\u043d\u0442\u0435\u0441\u044c \u0432 Google Drive", None))
#endif // QT_CONFIG(tooltip)
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0434\u0438\u0442\u0435 \u0432 Google \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label_treeWidget.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0438 \u043b\u0438\u0441\u0442:", None))
        self.patternButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 PDF \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u0435 \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.label_copyNumber.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u043c\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432:", None))
        self.copyNumber.setInputMask(QCoreApplication.translate("MainWindow", u"999999", None))
        self.copyNumber.setText("")
        self.dirButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044e \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c PDF \u0444\u0430\u0439\u043b\u044b...", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

