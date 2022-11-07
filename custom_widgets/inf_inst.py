from PyQt5.QtWidgets import QScrollArea, QGridLayout, QPushButton, QWidget, QLabel, QLineEdit


class ScrollArea(QScrollArea):
    """Класс используется для скроллинга вузов"""

    def __init__(self, parent=None):
        super(ScrollArea, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Создаем сетку для размещения виджетов
        grid = QGridLayout()

        foto = QLineEdit('')
        grid.addWidget(foto, 0, 0, 2, 2)

        for i in range(3):


            nazv = QLabel("Название Училища")
            grid.addWidget(nazv, 2 + i * 11, 0, 1, 1)
            nazv1 = QLineEdit('')
            grid.addWidget(nazv1, 3 + i * 11, 0, 1, 2)

            stran = QLabel("Страна")
            grid.addWidget(stran, 4 + i * 11, 0, 1, 1)
            stran1 = QLineEdit('')
            grid.addWidget(stran1, 5 + i * 11, 0, 1, 1)

            city = QLabel("Город")
            grid.addWidget(city, 4 + i * 11, 1, 1, 1)
            city1 = QLineEdit('')
            grid.addWidget(city1, 5 + i * 11, 1, 1, 1)

            pred = QLabel("Предметы")
            grid.addWidget(pred, 6 + i * 11, 0, 1, 1)
            pred1 = QLineEdit('')
            grid.addWidget(pred1, 7 + i * 11, 0, 1, 2)

            price = QLabel("Цена")
            grid.addWidget(price, 8 + i * 11, 0, 1, 1)
            price1 = QLineEdit('')
            grid.addWidget(price1, 9 + i * 11, 0, 1, 2)

            ball = QLabel("Балл")
            grid.addWidget(ball, 10 + i * 11, 0, 1, 1)
            ball1 = QLineEdit('')
            grid.addWidget(ball1, 11 + i * 11, 0, 1, 2)

        # Создал пустой виджет, установил на него сетку и сказал, что она теперь отображается в ScrollArea
        w = QWidget()
        w.setLayout(grid)
        self.setWidget(w)