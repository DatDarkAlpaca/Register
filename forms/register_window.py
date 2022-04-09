from res.compiled.register_window import Ui_RegisterDialog
from PySide6.QtWidgets import QDialog
from utils.database import register_user


class RegisterDialog(QDialog, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)

    def register_user(self):
        obj = {
            'first_name': self.first_name_edit.text(),
            'last_name': self.last_name_edit.text(),
            'age': self.age_edit.text()
        }

        register_user(self.first_name_edit.text(), obj, 'res/users.json')

    def clean_edits(self):
        self.first_name_edit.setText('')
        self.last_name_edit.setText('')
        self.age_edit.setText('')
