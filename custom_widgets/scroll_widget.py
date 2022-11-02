from PyQt5.QtWidgets import QScrollArea, QGridLayout, QPushButton, QWidget


class ScrollArea(QScrollArea):
    """Класс используется для скроллинга вузов"""

    def __init__(self, parent=None):
        super(ScrollArea, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # Создаем сетку для размещения виджетов
        grid = QGridLayout()

        # Тут я для примера просто добавил 50 кнопок. Вместо этого нам надо будет добавлять
        # виджеты с универами.
        for i in range(10):
            for j in range(5):
                btn = QPushButton(f"{i + 1}x{j + 1}")
                grid.addWidget(btn, i, j)

        # Создал пустой виджет, установил на него сетку и сказал, что она теперь отображается в ScrollArea
        w = QWidget()
        w.setLayout(grid)
        self.setWidget(w)
