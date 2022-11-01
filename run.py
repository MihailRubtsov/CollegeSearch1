import sys

from PyQt5.QtWidgets import QApplication
from custom_widgets.Glav_window import MyMainWindow


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
