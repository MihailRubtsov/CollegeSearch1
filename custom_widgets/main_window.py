from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QStackedWidget
from custom_widgets.scroll_widget import ScrollArea
from controls.pagination import PaginationController


class MyMainWindow(QMainWindow):
    """Главное окно. Отображает список университетов и меню."""
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер
        super(MyMainWindow, self).__init__(parent)
        self.stack = QStackedWidget(self)
        self.init_ui()
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Выбор института")

    def init_ui(self):
        grid = QGridLayout()
        widget = QWidget()

        scroll = ScrollArea(self)
        self.stack.addWidget(scroll)
        grid.addWidget(self.stack, 0, 0, 5, 1)
        grid.addWidget(PaginationController(self), 6, 0, 1, 1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)
