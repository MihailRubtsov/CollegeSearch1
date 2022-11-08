from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel


class Preview(QWidget):

    def __init__(self, parent=None):
        super(Preview, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        label = QLabel("Тест")
        btn = QPushButton("Подробнее")

        grid.addWidget(label, 0, 0, 1, 3)
        grid.addWidget(btn, 2, 4, 1, 4)

        self.setLayout(grid)
