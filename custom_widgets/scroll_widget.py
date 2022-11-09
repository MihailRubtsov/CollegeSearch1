from PyQt5.QtWidgets import QScrollArea, QGridLayout, QPushButton, QWidget, QMainWindow
from custom_widgets.detail_view import UniversityDetailView
from custom_widgets.university_preview import Preview
from config import db_manager


class ScrollArea(QScrollArea):
    """Класс используется для скроллинга вузов"""

    def __init__(self, parent: QMainWindow = None, start_index_of_data: int = 0):
        super(ScrollArea, self).__init__(parent)
        self.main_widget = QWidget(self)
        self.grid = QGridLayout(self)
        self.count_of_records = 0
        self.last_id_of_record = 0
        self.init_previews(start_index_of_data)
        self.init_ui()
        self.main_window = parent

    def init_previews(self, start_index_of_data: int):
        # TODO: Сделать код более модульным
        data = db_manager.get_university(start_index_of_data, 5)
        for i in range(len(data)):
            self.grid.addWidget(Preview(
                data[i]['id'],
                data[i]['title'],
                data[i]['country'],
                data[i]['city'],
                data[i]['minimum_price'],
                self, self.show_detail_view
            ), i, 0)
        self.last_id_of_record = data[-1]['id']
        self.count_of_records = len(data)

    def init_ui(self):
        # Создал пустой виджет, установил на него сетку и сказал, что она теперь отображается в ScrollArea
        self.main_widget.setLayout(self.grid)
        self.setWidget(self.main_widget)

    def show_detail_view(self):
        self.main_window.stack.addWidget(UniversityDetailView(parent=self.main_window,
                                                              previous_widget=self.main_window.centralWidget(),
                                         info_about_university=self.sender().parent().info))
        self.main_window.stack.setCurrentIndex(2)
