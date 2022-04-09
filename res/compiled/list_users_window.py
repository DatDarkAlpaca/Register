# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_users_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ListUserDialog(object):
    def setupUi(self, ListUserDialog):
        if not ListUserDialog.objectName():
            ListUserDialog.setObjectName(u"ListUserDialog")
        ListUserDialog.resize(240, 320)
        self.verticalLayout = QVBoxLayout(ListUserDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_list = QListWidget(ListUserDialog)
        self.user_list.setObjectName(u"user_list")

        self.verticalLayout.addWidget(self.user_list)

        self.button_box = QDialogButtonBox(ListUserDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(ListUserDialog)
        self.button_box.accepted.connect(ListUserDialog.accept)
        self.button_box.rejected.connect(ListUserDialog.reject)

        QMetaObject.connectSlotsByName(ListUserDialog)
    # setupUi

    def retranslateUi(self, ListUserDialog):
        ListUserDialog.setWindowTitle(QCoreApplication.translate("ListUserDialog", u"User List", None))
    # retranslateUi

