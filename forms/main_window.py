import sys

from res.compiled.main_window import Ui_MainWindow
from forms.list_user_window import ListUserDialog
from forms.register_window import RegisterDialog
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.connect_buttons()

    def connect_buttons(self):
        self.register_btn.clicked.connect(self._event_register_user)
        self.list_btn.clicked.connect(self._event_list_user)
        self.exit_btn.clicked.connect(sys.exit)

    # Handle events:
    def _event_register_user(self):
        register_dialog = RegisterDialog(self)

        if register_dialog.exec():
            register_dialog.register_user()
            register_dialog.clean_edits()
            return

    def _event_list_user(self):
        list_user_dialog = ListUserDialog(self)

        if list_user_dialog.exec():
            return
