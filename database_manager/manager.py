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

    def get_list_of_required_scores(self, university_id: int):
        """Получаем все проходные баллы для кадого ВУЗа"""

        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        raw_data = cur.execute(f"""SELECT * FROM required_score 
        WHERE university_id={university_id} ORDER BY course_id;""").fetchall()

        res = {}

        for record in raw_data:
            course_title = cur.execute(f"""SELECT (title) FROM course WHERE id = {record[-2]};""").fetchone()[0].title()
            try:
                res[course_title].update({record[1]: record[2]})
            except KeyError:
                res[course_title] = {
                    record[1]: record[2]
                }
        con.close()
        return res

    def get_all_universities(self):
        """Получаем кортеж всех ВУЗов"""

        con = sqlite3.connect(self.db_path)
        cur = con.cursor()

