from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QSizePolicy, QTableWidget
from PyQt5 import Qt, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView


class ControlWidget(QWidget):
    def __init__(self, parent=None, previous_widget=None):
        super(ControlWidget, self).__init__(parent)
        self.previous_widget = previous_widget
        self.back = QPushButton("Назад")
        self.back.clicked.connect(self.return_to_previous_widget)
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(self.back, 0, 0, 1, 1)
        grid.addLayout(QVBoxLayout(), 0, 2, 1, 3)
        self.setLayout(grid)

    def return_to_previous_widget(self):
        """Получаем стек виджетов на главном окне.
        Меняем главный виджет на список ВУЗов и удаляем виджет с текущим ВУЗом."""
        main_window_stack = self.parent().parent()
        tmp = main_window_stack.currentWidget()
        main_window_stack.setCurrentIndex(0)
        main_window_stack.removeWidget(tmp)


class UniversityDetailView(QWidget):
    def __init__(self, parent=None, previous_widget=None, info_about_university: dict={}):
        super(UniversityDetailView, self).__init__(parent)
        self.previous_widget = previous_widget
        self.info = info_about_university
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        print(self.info)

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

        self.tableWidget = QTableWidget()

        # Row count
        self.tableWidget.setRowCount(4)

        # Column count
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Aloysius"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Bhopal"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Mandsaur"))

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        grid.addWidget(self.tableWidget, 5, 0, 1, 2)

        grid.addWidget(ControlWidget(parent=self.parent(), previous_widget=self.previous_widget), 0, 0, 1, 5)

        self.setLayout(grid)
