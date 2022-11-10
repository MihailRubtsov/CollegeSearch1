from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QStackedWidget
from custom_widgets.scroll_widget import ScrollArea
from controls.pagination import PaginationController
from controls.main_menu import MainMenu


MAX_PAGE_COUNT = 10
COUNT_OF_UNIVERSITIES_AT_PAGE = 5


class MyMainWindow(QMainWindow):
    """Главное окно. Отображает список университетов и меню."""
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер
        super(MyMainWindow, self).__init__(parent)
        self.main_menu = None
        self.pagination_controller = None
        self.stack = QStackedWidget(self)
        self.init_ui()
        self.setMinimumSize(550, 550)
        self.setWindowTitle("Выбор института")

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(0)
        widget = QWidget()

        start_index = 0

        for i in range(MAX_PAGE_COUNT):
            scroll = ScrollArea(self, start_index)
            start_index = scroll.last_id_of_record + 1
            self.stack.addWidget(scroll)
            if scroll.count_of_records != 5:
                break

        self.main_menu = MainMenu(self)
        grid.addWidget(self.main_menu, 0, 0, 1, 1)
        grid.addWidget(self.stack, 1, 0, 5, 1)
        self.pagination_controller = PaginationController(self)
        grid.addWidget(self.pagination_controller, 7, 0, 1, 1)
        widget.setLayout(grid)
        self.setCentralWidget(widget)
