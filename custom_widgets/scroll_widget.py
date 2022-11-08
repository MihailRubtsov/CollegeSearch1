from PyQt5.QtWidgets import QScrollArea, QGridLayout, QPushButton, QWidget, QMainWindow
from custom_widgets.detail_view import UniversityDetailView


class ScrollArea(QScrollArea):
    """Класс используется для скроллинга вузов"""

    def __init__(self, parent: QMainWindow = None):
        super(ScrollArea, self).__init__(parent)
        self.universities = [[QPushButton(self) for _ in range(5)] for _ in range(10)]
        self.main_widget = QWidget(self)
        self.grid = QGridLayout(self)
        self.init_buttons()
        self.init_ui()
        self.main_window = parent

    def init_buttons(self):
        for i in range(10):
            for j in range(5):
                self.universities[i][j].setText(f"{i + 1}x{j + 1}")
                self.universities[i][j].clicked.connect(self.show_detail_view)
                self.grid.addWidget(self.universities[i][j], i, j, 1, 1)

    def init_ui(self):
        # Создал пустой виджет, установил на него сетку и сказал, что она теперь отображается в ScrollArea
        self.main_widget.setLayout(self.grid)
        self.setWidget(self.main_widget)

    def show_detail_view(self):
        self.main_window.stack.addWidget(UniversityDetailView(parent=self.main_window,
                                                              previous_widget=self.main_window.centralWidget()))
        self.main_window.stack.setCurrentIndex(1)
