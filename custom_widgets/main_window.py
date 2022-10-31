from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер
        super(MyMainWindow, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        grid = QGridLayout()

        btn = QPushButton("Бюджет")
        btn2 = QPushButton("Платка")
        btn3 = QPushButton("Целевое")

        grid.addWidget(btn, 0, 0, 2, 2)
        grid.addWidget(btn2, 0, 2, 2, 2)

        lbl = QLabel("Hello")
        lbl2 = QLabel("OK")

        grid.addWidget(lbl2, 1, 0, 1, 1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)
