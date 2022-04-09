from res.compiled.list_users_window import Ui_ListUserDialog
from PySide6.QtWidgets import QDialog, QListWidgetItem
from utils.database import load_users


class ListUserDialog(QDialog, Ui_ListUserDialog):
    def __init__(self, parent=None):
        super(ListUserDialog, self).__init__(parent)
        self.setupUi(self)

        self._refresh_data()

    def _refresh_data(self):
        data = load_users('res/users.json')
        for i, (user, user_data) in enumerate(data.items()):
            item = QListWidgetItem(f"ID: #{i}\n"
                                   f"Name: {user_data['first_name']} {user_data['last_name']}\n"
                                   f"Age: {user_data['age']}\n")
            self.user_list.insertItem(self.user_list.count(), item)
