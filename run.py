import sys
import sqlite3 as sql

from PyQt5.QtWidgets import QApplication
from custom_widgets.registra_window import MyMainWindow


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # con = sql.connect('Instituti.db')
    # cur = con.cursor()
    # cur.execute(f"""CREATE TABLE user (
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # username CHAR(80) UNIQUE NOT NULL,
    # name CHAR(80),
    # surname CHAR(80),
    # middle_name CHAR(80),
    # city CHAR(50),
    # email CHAR(250),
    # password CHAR(300) NOT NULL
    # );""")
    # con.commit()
    # con.close()
    main()
