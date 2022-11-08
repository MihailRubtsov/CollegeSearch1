import sqlite3


class Manager():

    def __init__(self, database_path):
        self.db_path = database_path

    def get_university(self, start_index: int, end_index: int) -> tuple:
        """Получение записей об университетах, начиная со start_index до end_index"""
        if end_index < start_index:
            raise IndexError("Стартовый индекс не может больше конечного.")

        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        raw_data = cur.execute(f"""SELECT * FROM university WHERE id>={start_index} AND id<={end_index};""").fetchall()
        con.close()

        res = []
        for record in raw_data:
            data = {'title': record[1], 'country': record[2], 'city': record[3], 'minimum_price': record[4]}
            res.append(data)

        return tuple(res)
