import sqlite3


class Manager:

    def __init__(self, database_path):
        self.db_path = database_path

    def get_university(self, start_index: int, count: int) -> tuple:
        """Получение записей об университетах, начиная со start_index до end_index"""
        if count < 0:
            raise IndexError("Стартовый индекс не может больше конечного.")

        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        raw_data = cur.execute(f"""SELECT * FROM university WHERE id>={start_index} LIMIT {count};""").fetchall()
        con.close()

        res = []
        for record in raw_data:
            data = {
                'id': record[0],
                'title': record[1],
                'country': record[2],
                'city': record[3],
                'minimum_price': record[4] if len(record) > 4 else '-',
            }
            res.append(data)

        return tuple(res)
