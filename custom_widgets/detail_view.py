from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QSizePolicy, QTableWidget
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from config import db_manager


class ControlWidget(QWidget):
    def __init__(self, parent=None, previous_widget=None):
        super(ControlWidget, self).__init__(parent)
        self.main_window = parent
        self.previous_widget = previous_widget
        self.back = QPushButton(
            "Назад")  # Создание кнопки назад с помощью которой можем венуться из подробного просмотра университета
        self.back.clicked.connect(self.return_to_previous_widget)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(self.back, 0, 0, 1, 1)
        grid.addLayout(QVBoxLayout(), 0, 2, 1, 3)
        self.setLayout(grid)

    def return_to_previous_widget(self):
        main_window_stack = self.parent().parent()
        tmp = main_window_stack.currentWidget()
        main_window_stack.setCurrentIndex(0)
        main_window_stack.removeWidget(tmp)
        self.main_window.pagination_controller.show()


class UniversityDetailView(QWidget):
    def __init__(self, parent=None, previous_widget=None, info_about_university: dict = {}):
        super(UniversityDetailView, self).__init__(parent)
        self.tableWidget = None
        self.previous_widget = previous_widget
        self.info = info_about_university  # self.info['id']
        self.required_scores = db_manager.get_list_of_required_scores(self.info['id'])
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        # Создание названия города и цены и изменение их штриха

        nazv1 = QLabel(self.info['title'])
        nazv1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        nazv1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        nazv1.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(nazv1, 2, 0, 1, 2)

        city1 = QLabel(self.info['city'])
        city1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        city1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        grid.addWidget(city1, 3, 0, 1, 1)

        price2 = "От " + str(self.info['min_price']) + " Рублей в год"
        price1 = QLabel(price2)
        price1.setStyleSheet("font-weight: bold;")
        price1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        price1.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        grid.addWidget(price1, 4, 0, 1, 2)

        # Создание таблицы с последующий заполнением её значениями из БД

        self.tableWidget = QTableWidget()

        database_items = self.required_scores.items()
        unique_years = set()
        for item in database_items:
            unique_years.update(item[1].keys())
        maximum_year_count = len(unique_years)

        # Row count
        self.tableWidget.setRowCount(len(database_items))

        # Column count
        self.tableWidget.setColumnCount(maximum_year_count)
        for i, year in enumerate(reversed(tuple(unique_years))):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(str(year)))

        for i, item in enumerate(database_items):
            self.tableWidget.setVerticalHeaderItem(i, QTableWidgetItem(item[0]))
            for j, year_score in enumerate(item[1].items()):
                index = 0
                for col in range(self.tableWidget.columnCount()):
                    if int(self.tableWidget.horizontalHeaderItem(
                            self.tableWidget.horizontalHeader().logicalIndex(col)).text()) == year_score[0]:
                        index = col
                        break
                self.tableWidget.setItem(i, index, QTableWidgetItem(str(year_score[1])))

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        grid.addWidget(self.tableWidget, 5, 0, 1, 5)

        control_widget = ControlWidget(parent=self.parent(), previous_widget=self.previous_widget)
        control_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        grid.addWidget(control_widget, 0, 0, 1, 5)

        self.setLayout(grid)
