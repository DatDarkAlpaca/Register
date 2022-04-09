# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 250)
        MainWindow.setMinimumSize(QSize(340, 250))
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_label = QLabel(self.central_widget)
        self.central_label.setObjectName(u"central_label")
        font = QFont()
        font.setPointSize(16)
        self.central_label.setFont(font)
        self.central_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.central_label)

        self.register_btn = QPushButton(self.central_widget)
        self.register_btn.setObjectName(u"register_btn")

        self.verticalLayout.addWidget(self.register_btn)

        self.list_btn = QPushButton(self.central_widget)
        self.list_btn.setObjectName(u"list_btn")

        self.verticalLayout.addWidget(self.list_btn)

        self.exit_btn = QPushButton(self.central_widget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.verticalLayout.addWidget(self.exit_btn)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Register", None))
        self.central_label.setText(QCoreApplication.translate("MainWindow", u"Register Application", None))
        self.register_btn.setText(QCoreApplication.translate("MainWindow", u"Register New User", None))
        self.list_btn.setText(QCoreApplication.translate("MainWindow", u"List Users", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

