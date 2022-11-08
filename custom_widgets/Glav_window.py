from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QCheckBox, QLineEdit


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер

        super(MyMainWindow, self).__init__(parent)
        self.init_ui()
        self.setWindowTitle("Вход")
        self.setGeometry(300, 300, 330, 330)



    def init_ui(self):
        widget = QWidget()
        grid = QGridLayout()

        inst = QLabel("Найди себе университет")
        grid.addWidget(inst, 2, 2, 1, 1)
        reg = QPushButton("Регистрация")
        grid.addWidget(reg, 3, 1, 1, 1)
        vfod = QPushButton("Вход")
        grid.addWidget(vfod, 3, 3, 1, 1)






        widget.setLayout(grid)
        self.setCentralWidget(widget)