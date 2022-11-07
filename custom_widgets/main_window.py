from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QStackedWidget
from custom_widgets.scroll_widget import ScrollArea


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # TODO: сделать название приложения, установить минимальный размер
        super(MyMainWindow, self).__init__(parent)
        self.stack = QStackedWidget(self)
        self.init_ui()

    def init_ui(self):
        scroll = ScrollArea(self)
        scroll.setObjectName('university_list_view')
        self.stack.addWidget(scroll)
        self.setCentralWidget(self.stack)
