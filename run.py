import os
import sys

from PyQt5.QtWidgets import QApplication
from custom_widgets.main_window import MyMainWindow
from database_manager.manager import Manager


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
