from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QCheckBox, QLineEdit


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер

        super(MyMainWindow, self).__init__(parent)
        self.init_ui()
        self.setWindowTitle("Регистрация")
        self.setGeometry(300, 300, 330, 330)

    def init_ui(self):
        widget = QWidget()
        grid = QGridLayout()

        nik = QLabel("Ник")
        grid.addWidget(nik, 0, 0, 1, 1)
        nik1 = QLineEdit('')
        grid.addWidget(nik1, 1, 0, 1, 2)

        ima = QLabel("Ваше имя")
        grid.addWidget(ima, 2, 0, 1, 1)
        ima1 = QLineEdit('')
        grid.addWidget(ima1, 3, 0, 1, 2)

        familia = QLabel("Ваша Фамилия")
        grid.addWidget(familia, 4, 0, 1, 1)
        familia1 = QLineEdit('')
        grid.addWidget(familia1, 5, 0, 1, 2)

        otchestvo = QLabel("Ваше отчество")
        grid.addWidget(otchestvo, 6, 0, 1, 1)
        otchestvo1 = QLineEdit('')
        grid.addWidget(otchestvo1, 7, 0, 1, 2)

        gorod = QLabel("Напишите город")
        grid.addWidget(gorod, 8, 0, 1, 1)
        city1 = QLineEdit('')
        grid.addWidget(city1, 9, 0, 1, 2)

        parol = QLabel("Напишите пароль")
        grid.addWidget(parol, 10, 0, 1, 1)
        parol1 = QLineEdit('')
        grid.addWidget(parol1, 11, 0, 1, 2)

        pochta = QLabel("Напишите почта")
        grid.addWidget(pochta, 12, 0, 1, 1)
        pochta1 = QLineEdit('')
        grid.addWidget(pochta1, 13, 0, 1, 2)

        telefon = QLabel("Напишите телефон")
        grid.addWidget(telefon, 14, 0, 1, 1)
        telefon1 = QLineEdit('')
        grid.addWidget(telefon1, 15, 0, 1, 2)









        widget.setLayout(grid)
        self.setCentralWidget(widget)