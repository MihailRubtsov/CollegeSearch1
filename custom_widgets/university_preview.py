from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel


class Preview(QWidget):

    def __init__(self, parent=None, call_function=None):
        super(Preview, self).__init__(parent)
        self.call_function = call_function
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        name = QLabel("Название")
        price = QLabel("Цена ")
        city = QLabel("Город")
        btn = QPushButton("Подробнее об институте")
        btn.clicked.connect(self.call_function)

        grid.addWidget(name, 0, 0, 1, 3)
        grid.addWidget(price, 2, 0, 1, 4)
        grid.addWidget(city, 2, 3, 1, 1)
        grid.addWidget(btn, 2, 5, 1, 1)

        self.setLayout(grid)
