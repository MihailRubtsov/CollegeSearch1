from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QStackedWidget
from custom_widgets.scroll_widget import ScrollArea
from controls.pagination import PaginationController
from controls.main_menu import MainMenu

MAX_PAGE_COUNT = 10
COUNT_OF_UNIVERSITIES_AT_PAGE = 5


class MyMainWindow(QMainWindow):
    # Главное окно и его описание
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.scroll = None
        self.main_menu = None
        self.pagination_controller = None
        self.stack = QStackedWidget(self)
        self.init_ui()
        self.setMinimumSize(550, 550)
        self.setWindowTitle("Выбор института")

    def init_university_list(self):
        start_index = 0

        for i in range(MAX_PAGE_COUNT):
            self.scroll = ScrollArea(self, start_index)
            start_index = self.scroll.last_id_of_record + 1
            self.stack.addWidget(self.scroll)
            if self.scroll.count_of_records != 5:
                break

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(0)
        widget = QWidget()

        self.init_university_list()

        # self.main_menu = MainMenu(self)
        # grid.addWidget(self.main_menu, 0, 0, 1, 1)
        grid.addWidget(self.stack, 0, 0, 5, 1)
        self.pagination_controller = PaginationController(self)
        grid.addWidget(self.pagination_controller, 6, 0, 1, 1)
        widget.setLayout(grid)
        self.setCentralWidget(widget)
