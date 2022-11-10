from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLineEdit, QCompleter
from config import db_manager


class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.completer = QCompleter(db_manager.get_universities())
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addLayout(QHBoxLayout(), 0, 0, 1, 6)
        search_field = QLineEdit()
        search_field.setCompleter(self.completer)
        search_field.setPlaceholderText("Найдите ВУЗ по названию...")
        search_field.editingFinished.connect(self.get_list_of_correct_universities)
        grid.addWidget(search_field, 0, 6, 1, 3)

        self.setLayout(grid)

    def get_list_of_correct_universities(self):
        try:
            print(db_manager.get_universities(f"""WHERE (title LIKE '%{self.sender().text().strip()}%')"""))
        except Exception as error:
            print(error)
