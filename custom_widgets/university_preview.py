from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel


class Preview(QWidget):

    def __init__(self, id_of_record: int, title: str, country: str, city: str, min_price: float, parent=None, call_function=None):
        super(Preview, self).__init__(parent)
        self.call_function = call_function
        self.id = id_of_record
        self.info = {
            'id': id_of_record,
            'title': title,
            'country': country,
            'city': city,
            'min_price': min_price,
        }
        self.init_ui(title, country, city, min_price)

    def init_ui(self, title, country, city, min_price):
        grid = QGridLayout()
        grid.setSpacing(10)

        name = QLabel(title)
        name.setStyleSheet("font-weight: bold;")
        price = QLabel(str(min_price) + "₽")
        city = QLabel(city)
        btn = QPushButton(self)
        btn.setText("Подробнее")
        btn.clicked.connect(self.call_function)

        grid.addWidget(name, 0, 0, 1, 3)
        grid.addWidget(price, 2, 0, 1, 4)
        grid.addWidget(city, 2, 3, 1, 1)
        grid.addWidget(btn, 2, 5, 1, 1)

        self.setLayout(grid)
