# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_window.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        if not RegisterDialog.objectName():
            RegisterDialog.setObjectName(u"RegisterDialog")
        RegisterDialog.resize(350, 300)
        RegisterDialog.setMinimumSize(QSize(350, 300))
        self.verticalLayout = QVBoxLayout(RegisterDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.title_spacer)

        self.title_label = QLabel(RegisterDialog)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.top_spacer)

        self.first_name_layout = QHBoxLayout()
        self.first_name_layout.setObjectName(u"first_name_layout")
        self.first_name_label = QLabel(RegisterDialog)
        self.first_name_label.setObjectName(u"first_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_name_label.sizePolicy().hasHeightForWidth())
        self.first_name_label.setSizePolicy(sizePolicy)
        self.first_name_label.setMinimumSize(QSize(90, 0))
        self.first_name_label.setMaximumSize(QSize(90, 16777215))

        self.first_name_layout.addWidget(self.first_name_label)

        self.first_name_edit = QLineEdit(RegisterDialog)
        self.first_name_edit.setObjectName(u"first_name_edit")

        self.first_name_layout.addWidget(self.first_name_edit)


        self.verticalLayout.addLayout(self.first_name_layout)

        self.last_name_layout = QHBoxLayout()
        self.last_name_layout.setObjectName(u"last_name_layout")
        self.last_name_label = QLabel(RegisterDialog)
        self.last_name_label.setObjectName(u"last_name_label")
        sizePolicy.setHeightForWidth(self.last_name_label.sizePolicy().hasHeightForWidth())
        self.last_name_label.setSizePolicy(sizePolicy)
        self.last_name_label.setMinimumSize(QSize(90, 0))
        self.last_name_label.setMaximumSize(QSize(90, 16777215))

        self.last_name_layout.addWidget(self.last_name_label)

        self.last_name_edit = QLineEdit(RegisterDialog)
        self.last_name_edit.setObjectName(u"last_name_edit")

        self.last_name_layout.addWidget(self.last_name_edit)


        self.verticalLayout.addLayout(self.last_name_layout)

        self.age_name_layout = QHBoxLayout()
        self.age_name_layout.setObjectName(u"age_name_layout")
        self.age_label = QLabel(RegisterDialog)
        self.age_label.setObjectName(u"age_label")
        sizePolicy.setHeightForWidth(self.age_label.sizePolicy().hasHeightForWidth())
        self.age_label.setSizePolicy(sizePolicy)
        self.age_label.setMinimumSize(QSize(90, 0))
        self.age_label.setMaximumSize(QSize(90, 16777215))

        self.age_name_layout.addWidget(self.age_label)

        self.age_edit = QLineEdit(RegisterDialog)
        self.age_edit.setObjectName(u"age_edit")

        self.age_name_layout.addWidget(self.age_edit)


        self.verticalLayout.addLayout(self.age_name_layout)

        self.bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.bottom_spacer)

        self.button_box = QDialogButtonBox(RegisterDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setLayoutDirection(Qt.LeftToRight)
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.button_box.setCenterButtons(True)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(RegisterDialog)
        self.button_box.accepted.connect(RegisterDialog.accept)
        self.button_box.rejected.connect(RegisterDialog.reject)

        QMetaObject.connectSlotsByName(RegisterDialog)
    # setupUi

    def retranslateUi(self, RegisterDialog):
        RegisterDialog.setWindowTitle(QCoreApplication.translate("RegisterDialog", u"Register User", None))
        self.title_label.setText(QCoreApplication.translate("RegisterDialog", u"Register New User", None))
        self.first_name_label.setText(QCoreApplication.translate("RegisterDialog", u"First Name", None))
        self.last_name_label.setText(QCoreApplication.translate("RegisterDialog", u"Last Name", None))
        self.age_label.setText(QCoreApplication.translate("RegisterDialog", u"Age", None))
    # retranslateUi

