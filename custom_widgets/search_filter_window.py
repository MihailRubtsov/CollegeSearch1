from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QCheckBox, QLineEdit


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер

        super(MyMainWindow, self).__init__(parent)
        self.init_ui()
        self.setWindowTitle("Выбор института")
        self.setGeometry(300, 300, 330, 330)

    def init_ui(self):
        widget = QWidget()
        grid = QGridLayout()

        inst = QLabel("Вид платы")
        grid.addWidget(inst, 0, 0, 1, 1)

        boxbu = QCheckBox("Бюджет")
        boxpl = QCheckBox("Платка")
        boxche = QCheckBox("Целевое")

        grid.addWidget(boxpl, 1, 0, 1, 1)
        grid.addWidget(boxbu, 1, 1, 1, 1)
        grid.addWidget(boxche, 1, 2, 1, 1)

        pred = QLabel("Предметы")
        grid.addWidget(pred, 2, 0, 1, 1)

        boxfiz = QCheckBox("Физика")
        boxprmat = QCheckBox("Профельная математика")
        boxhim = QCheckBox("Химия")
        boxlit = QCheckBox("Литиратура")
        boxangl = QCheckBox("Английский")
        boxinf = QCheckBox("Информатика")
        boxistr = QCheckBox("История")
        boxobch = QCheckBox("Обществознаие")

        grid.addWidget(boxfiz, 3, 0, 1, 1)
        grid.addWidget(boxprmat, 3, 1, 1, 1)
        grid.addWidget(boxhim, 3, 2, 1, 1)
        grid.addWidget(boxlit, 3, 3, 1, 1)
        grid.addWidget(boxangl, 4, 0, 1, 1)
        grid.addWidget(boxinf, 4, 1, 1, 1)
        grid.addWidget(boxistr, 4, 2, 1, 1)
        grid.addWidget(boxobch, 4, 3, 1, 1)

        lbl2 = QLabel("Напишите город")
        grid.addWidget(lbl2, 5, 0, 1, 1)
        city = QLineEdit('')
        grid.addWidget(city, 6, 0, 1, 2)

        prise = QLabel("Максимальная цена")
        grid.addWidget(prise, 7, 0, 1, 1)
        prise1 = QLineEdit('')
        grid.addWidget(prise1, 8, 0, 1, 2)

        bal = QLabel("Баллы которые вы набрали за ЕГЭ")
        grid.addWidget(bal, 9, 0, 1, 1)
        ball = QLineEdit('')
        grid.addWidget(ball, 10, 0, 1, 2)

        reting = QLabel("Рейтинг")
        grid.addWidget(reting, 11, 0, 1, 1)
        reting1 = QLineEdit('')
        grid.addWidget(reting1, 12, 0, 1, 1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)
