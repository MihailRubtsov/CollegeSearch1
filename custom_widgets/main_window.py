from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QStackedWidget
from custom_widgets.scroll_widget import ScrollArea
from controls.pagination import PaginationController
from controls.main_menu import MainMenu


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
        grid.addWidget(MainMenu(self), 0, 0, 1, 1)
        grid.addWidget(self.stack, 1, 0, 5, 1)
        grid.addWidget(PaginationController(self), 7, 0, 1, 1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)
