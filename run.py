import sys

from PyQt5.QtWidgets import QApplication
from custom_widgets.scroll_widget import ScrollArea


def main():
    app = QApplication(sys.argv)
    window = ScrollArea()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
