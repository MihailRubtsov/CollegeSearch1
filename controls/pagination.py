from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QHBoxLayout


class PaginationController(QWidget):

    def __init__(self, parent=None):
        super(PaginationController, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addLayout(QHBoxLayout(), 0, 0, 1, 2)

        grid.addWidget(QPushButton("<-"), 0, 2, 1, 1)

        label = QLabel("0 из 3")
        label.setAlignment(Qt.Qt.AlignCenter)
        grid.addWidget(label, 0, 3, 1, 2)

        grid.addWidget(QPushButton("->"), 0, 5, 1, 1)

        grid.addLayout(QHBoxLayout(), 0, 6, 1, 2)

        self.setLayout(grid)
