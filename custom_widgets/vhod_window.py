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

        inst = QLabel("Вход в учётную запись")
        grid.addWidget(inst, 1, 2, 1, 1)

        b = QLineEdit('')
        grid.addWidget(b, 0, 1, 0, 0)

        b1 = QLineEdit('')
        grid.addWidget(b1, 0, 3, 0, 0)

        email = QLabel("Введите свой емейл")
        grid.addWidget(email, 2, 0, 1, 1)
        email1 = QLineEdit('')
        grid.addWidget(email1, 3, 0, 1, 2)

        parol = QLabel("введить свой пароль")
        grid.addWidget(parol, 4, 0, 1, 1)
        parol1 = QLineEdit('')
        grid.addWidget(parol1, 5, 0, 1, 2)

        vhod = QPushButton("Войти")
        grid.addWidget(vhod, 6, 2, 1, 1)



        widget.setLayout(grid)
        self.setCentralWidget(widget)
