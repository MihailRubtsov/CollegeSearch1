from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLabel, QVBoxLayout


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
    def __init__(self, parent=None, previous_widget=None):
        super(UniversityDetailView, self).__init__(parent)
        self.previous_widget = previous_widget
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        label = QLabel("Тестовый универ")
        description = QLabel("Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum. Lorem ipsum.")
        btn = QPushButton("Оставить отзыв")

        grid.addWidget(ControlWidget(parent=self.parent(), previous_widget=self.previous_widget), 0, 0, 1, 5)
        grid.addWidget(label, 1, 1, 2, 2)
        grid.addWidget(description, 4, 0, 5, 5)
        grid.addWidget(btn, 10, 4, 1, 1)

        self.setLayout(grid)
