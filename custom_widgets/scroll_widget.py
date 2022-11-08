from PyQt5.QtWidgets import QScrollArea, QGridLayout, QPushButton, QWidget, QMainWindow
from custom_widgets.detail_view import UniversityDetailView
from custom_widgets.university_preview import Preview


class ScrollArea(QScrollArea):
    """Класс используется для скроллинга вузов"""

    def __init__(self, parent: QMainWindow = None):
        super(ScrollArea, self).__init__(parent)
        self.main_widget = QWidget(self)
        self.grid = QGridLayout(self)
        self.init_buttons()
        self.init_ui()
        self.main_window = parent

    def init_buttons(self):
        for i in range(5):
            self.grid.addWidget(Preview(self, self.show_detail_view), i, 0, 1, 1)

    def init_ui(self):
        # Создал пустой виджет, установил на него сетку и сказал, что она теперь отображается в ScrollArea
        self.main_widget.setLayout(self.grid)
        self.setWidget(self.main_widget)

    def show_detail_view(self):
        self.main_window.stack.addWidget(UniversityDetailView(parent=self.main_window,
                                                              previous_widget=self.main_window.centralWidget()))
        self.main_window.stack.setCurrentIndex(1)
