from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QPushButton, QLineEdit


class MainMenu(QWidget):

    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addLayout(QHBoxLayout(), 0, 0, 1, 6)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Найдите ВУЗ по названию...")
        grid.addWidget(search_field, 0, 6, 1, 3)

        self.setLayout(grid)
