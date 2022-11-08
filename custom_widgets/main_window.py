from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QStackedWidget
from custom_widgets.scroll_widget import ScrollArea


class MyMainWindow(QMainWindow):
    """Главное окно. Отображает список университетов и меню."""
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер
        super(MyMainWindow, self).__init__(parent)
        self.stack = QStackedWidget(self)
        self.init_ui()

    def init_ui(self):
        scroll = ScrollArea(self)
        self.stack.addWidget(scroll)
        self.setCentralWidget(self.stack)
