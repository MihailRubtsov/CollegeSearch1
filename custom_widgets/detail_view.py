from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit


class ControlWidget(QWidget):
    def __init__(self, parent=None, previous_widget=None):
        super(ControlWidget, self).__init__(parent)
        self.previous_widget = previous_widget
        self.back = QPushButton("Назад")
        self.back.clicked.connect(self.return_to_previous_widget)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(self.back, 0, 0, 1, 1)
        grid.addLayout(QVBoxLayout(), 0, 2, 1, 3)
        self.setLayout(grid)

    def return_to_previous_widget(self):
        """Получаем стек виджетов на главном окне.
        Меняем главный виджет на список ВУЗов и удаляем виджет с текущим ВУЗом."""
        main_window_stack = self.parent().parent()
        tmp = main_window_stack.currentWidget()
        main_window_stack.setCurrentIndex(0)
        main_window_stack.removeWidget(tmp)


class UniversityDetailView(QWidget):
    def __init__(self, parent=None, previous_widget=None, info_about_university: dict = {}):
        super(UniversityDetailView, self).__init__(parent)
        self.previous_widget = previous_widget
        self.info = info_about_university
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        foto = QLabel('test')
        grid.addWidget(foto, 1, 0, 2, 2)

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

        grid.addWidget(ControlWidget(parent=self.parent(), previous_widget=self.previous_widget), 0, 0, 1, 5)

        self.setLayout(grid)
