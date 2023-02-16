# kom ihåg att ha id automatisk i varje tabell
# medicin ska ha ett kapacitet för null 

import sqlite3 
import os 

class DB: 
    db_url: str 
    
    def __init__ (self, db_url: str): 
          self.db_url = db_url 

          if not os.path.exists(self.db_url): 
              self.init_db()

    def call_db(self, query, *args): 
          conn = sqlite3.connect(self.db_url)
          cur = conn.cursor()
          res = cur.execute(query, args)
          data = res. fetchall()
          cur.close()
          conn.commit()
          conn.close()
          return data 
    
    def init_db(self): #just need to check that it won't make this a integer. I think If it's in the seed, it will see this and not create an integer primary key
            init_db_query_1 = """
            CREATE TABLE IF NOT EXISTS elev (
                personnummer INTEGER PRIMARY KEY,  
                efternamn TEXT NOT NULL,
                förstanamn TEXT NOT NULL,
                ålder INTEGER NOT NULL,
                grundskola TEXT NOT NULL  
            );
            """
            #mål med prognos är att kunna ha unik siffror för varje sjukdom. Kan senare göra visualisering av olika sjukdommar i regionen.
            init_db_query_2 = """ 
            CREATE TABLE IF NOT EXISTS journaler (
                journal_id INTEGER PRIMARY KEY,
                datum DATETIME NOT NULL,
                student_personnummer INTEGER NOT NULL,
                specialist TEXT NOT NULL,
                prognos INTEGER NOT NULL, 
                anteckningar TEXT NOT NULL,
                medicin TEXT NOT NULL, 
                nytidskapad BOLEAN NOT NULL, 
                FOREIGN KEY(student_personnummer) REFERENCES elev(personnummer),
                FOREIGN KEY(specialist) REFERENCES specialist(id_specialist)
            );
            """
            init_db_query_3 = """
            CREATE TABLE IF NOT EXISTS specialist (
                id_specialist TEXT PRIMARY KEY,
                efternamn TEXT NOT NULL,
                förstanamn TEXT NOT NULL,
                titel TEXT NOT NULL,
                specialisering TEXT NOT NULL
            );
            """

            # insert_query1 = """
            # INSERT INTO elev (personnummber, efternamn, förstanamn, ålder, grundskola)
            # VALUES ('123942051234', 'jones', 'jonny', 8, 'Bergkristallsskolan');
            # """

            self.call_db(init_db_query_1)
            self.call_db(init_db_query_2)
            self.call_db(init_db_query_3)
            
      