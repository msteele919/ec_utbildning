# kan hjälpa att titta på "seeda database med mac": https://academediase.sharepoint.com/:v:/s/DataScientist22-SolnaGteborg/EYksY_lcYApCm4g_ix0DxE8BSD71tS5B12QhV4PoIZT_uQ?e=SGJcYe


import pyodbc
# bröjar med server. kolla inom azure data studio 
db_server = "localhost,57000"
db_name = "lesson_todo"
db_driver = "ODBC Driver 17 for SQL Server"
connection_string = f"""
DRIVER = {db_driver}; 
SERVER = {db_server}; 
DATABASE={db_name };
trusted_connection = yes; 
"""


class DB: 

    def call_db(self, query, *args):
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        if "SELECT" in query: 
            res = cur.execute(query, args)
            data = res.fetchall()
            cur.close()
        else: 
            conn.execute(query, args)
        conn.commit()
        conn.close()
        return data 

    def init_db(self):
        init_db_query= """
        DROP TABLE todo;
        CREATE TABLE  todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(255) NOT NULL, 
            descript VARCHAR(255) NOT NULL
        );
        """
        insert_query = """
        INSERT INTO todo(title, descript) VALUES ( 'DO THIS', 'dont do that when doing this')
        """
        conn = pyodbc.connect(connection_string)
        conn.execute(init_db_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
       
if __name__ == "__main__": 
    db = DB() 
    db.init_db()