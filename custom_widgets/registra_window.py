from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QCheckBox, QLineEdit
import sqlite3 as sql


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

        self.nik = QLabel("Ник")
        grid.addWidget(self.nik, 0, 0, 1, 1)
        self.nik1 = QLineEdit('')
        grid.addWidget(self.nik1, 1, 0, 1, 2)

        self.ima = QLabel("Ваше имя")
        grid.addWidget(self.ima, 2, 0, 1, 1)
        self.ima1 = QLineEdit('')
        grid.addWidget(self.ima1, 3, 0, 1, 2)

        self.familia = QLabel("Ваша Фамилия")
        grid.addWidget(self.familia, 4, 0, 1, 1)
        self.familia1 = QLineEdit('')
        grid.addWidget(self.familia1, 5, 0, 1, 2)

        self.otchestvo = QLabel("Ваше отчество")
        grid.addWidget(self.otchestvo, 6, 0, 1, 1)
        self.otchestvo1 = QLineEdit('')
        grid.addWidget(self.otchestvo1, 7, 0, 1, 2)

        self.gorod = QLabel("Напишите город")
        grid.addWidget(self.gorod, 8, 0, 1, 1)
        self.city1 = QLineEdit('')
        grid.addWidget(self.city1, 9, 0, 1, 2)

        self.parol = QLabel("Напишите пароль")
        grid.addWidget(self.parol, 10, 0, 1, 1)
        self.parol1 = QLineEdit('')
        grid.addWidget(self.parol1, 11, 0, 1, 2)

        self.pochta = QLabel("Напишите почта")
        grid.addWidget(self.pochta, 12, 0, 1, 1)
        self.pochta1 = QLineEdit('')
        grid.addWidget(self.pochta1, 13, 0, 1, 2)

        self.telefon = QLabel("Напишите телефон")
        grid.addWidget(self.telefon, 14, 0, 1, 1)
        self.telefon1 = QLineEdit('')
        grid.addWidget(self.telefon1, 15, 0, 1, 2)

        self.registr = QPushButton("Регистрация")
        grid.addWidget(self.registr, 16, 0, 1, 1)
        self.registr.clicked.connect(self.sohr)

        widget.setLayout(grid)
        self.setCentralWidget(widget)


    def sohr(self):
        con = sql.connect('Instituti.db')

        cur = con.cursor()
        cur.execute(
        f"INSERT INTO Users (Name, Famil, Otch, City, Pasword, Mail, Phone, Nik) VALUES ('{self.ima1.text()}',"
        f" '{self.familia1.text()}', '{self.otchestvo1.text()}', '{self.city1.text()}', '{self.parol1.text()}', "
        f"'{self.pochta1.text()}', '{self.telefon1.text()}', '{self.nik1.text()}');")
        con.commit()
        con.close()
