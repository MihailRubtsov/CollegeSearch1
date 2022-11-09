from PyQt5 import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QHBoxLayout


class PaginationController(QWidget):

    def __init__(self, parent=None):
        super(PaginationController, self).__init__(parent)
        self.label = None
        self.back = QPushButton("<-")
        self.next = QPushButton("->")
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        grid.addLayout(QHBoxLayout(), 0, 0, 1, 2)

        self.back.clicked.connect(self.return_to_previous_page)
        grid.addWidget(self.back, 0, 2, 1, 1)

        self.label = QLabel(f"{self.parent().stack.currentIndex() + 1} из {self.parent().stack.count()}")
        self.label.setAlignment(Qt.Qt.AlignCenter)
        grid.addWidget(self.label, 0, 3, 1, 2)

        self.next.clicked.connect(self.go_to_next_page)
        grid.addWidget(self.next, 0, 5, 1, 1)

        grid.addLayout(QHBoxLayout(), 0, 6, 1, 2)

        self.setLayout(grid)

    def return_to_previous_page(self):
        print(self.parent().parent())
        if self.parent().parent().stack.currentIndex() != 0:
            self.parent().parent().stack.setCurrentIndex(self.parent().parent().stack.currentIndex() - 1)

    def go_to_next_page(self):
        if self.parent().parent().stack.currentIndex() + 1 < self.parent().parent().stack.count():
            self.parent().parent().stack.setCurrentIndex(self.parent().parent().stack.currentIndex() + 1)
