from PyQt5.QtWidgets import QScrollArea, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit


class ScrollArea(QScrollArea):

    def __init__(self, parent=None):
        super(ScrollArea, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Создаем сетку для размещения виджетов
        grid = QGridLayout()

        foto = QLineEdit('')
        grid.addWidget(foto, 0, 0, 2, 2)

        nazv1 = QLabel('Названия')
        grid.addWidget(nazv1, 2, 0, 1, 2)

        stran1 = QLabel('Страна')
        grid.addWidget(stran1, 3, 0, 1, 1)

        city1 = QLabel('Город')
        grid.addWidget(city1, 3, 1, 1, 1)

        pred1 = QLabel('Предметы нужные для поступления')
        grid.addWidget(pred1, 4, 0, 1, 2)

        price1 = QLabel('Цена')
        grid.addWidget(price1, 6, 0, 1, 2)

        ball1 = QLabel('Сумарный балл нужный для поступления')
        grid.addWidget(ball1, 5, 0, 1, 2)

        w = QWidget()
        w.setLayout(grid)
        self.setWidget(w)
