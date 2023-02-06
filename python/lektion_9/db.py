import sqlite3
import os
from typing import Dict, Tuple
class DB():

    db_url: str 

    def __init__(self, db_url):  #kommer att få url för database
        
        self.db_url= db_url

        # om man kör det här en gång kommer den att skapa databasen, och varje gång därefter återskapas
        # DB. Därför vill vi utföra en "check" varje gång vi använder den. Vi gör det med hjälp av OS
        if not os.path.exists(self.db_url):# OM DAABASEN INTE FINNS, SET UP 
            self.__set_up_db()

        # om det inte finns, kör vi koden nedanför 
        
    def __set_up_db(self): #läsa sql och execute den 
       conn = sqlite3.connect(self.db_url)
       with open("setup.sql", "r") as file: # hämta sql fil, with open skapar en context som automatist stänger filen senare
           # IF relative path doesn't work:  /Users/mstee/Documents/GitHub/ec_utbildning/python/lektion_9/setup.sql
           script = file.read()
           conn.executescript(script) #skicka in vår komman
           conn.commit() # commita

       conn.close() 

    def __call_db(self, query): #tror att __call_ alltså bara ett "_" betyder att den ska inte kunna 
        # kallas utifrån. den anropa bara från inuti våran cxlass
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data 
    
    ###### getting a 405 method not allowed. 

    def insert(self, *, table: str, fields: Dict[str, str]): 
        #skapa en query 
        # ta emot värden från vårat anrop
        # anropa databasen
        keys= ",".join(fields.keys())
        values= "','".join(fields.values()) #problem så länge är att ett null värde skapar error
        query = f"""
        INSERT INTO {table} (
            {keys} 
        ) VALUES (
            '{values}' 
        ) 
        """
        #tanken är att kollumnerna ska vara i en dictionary då ska keys bli kolliumner, och values  = värde
        #singel qvot behövs för att signalera värden.
        return self.__call_db(query)
        
    #is this a way to get the data in aanother way? 
          
    def get(self, *, table: str, where: Tuple[str, str]| None = None):
        query = f"""
        SELECT * FROM {table} 
        """
        if where: 
            key, val = where
            where_query = f"""
            WHERE {key} = {val}
            """
            query = query + where_query
        data = self.__call_db(query)
        return data 
    
    def delete(self, *, table: str, id: int):
        delete_query = f"""
        DELETE FROM {table} WHERE id = {id}
        """
        self.__call_db(delete_query)

    def update(self, *, table: str, where: Tuple[str, str], fields: Dict[str, str]):
        where_key, where_val = where
        field_query = ""
        for key, val in fields.items():
            field_query += f"{key} = '{val}',"
        field_query = field_query[:-1]
        update_query = f"""
        UPDATE {table} SET {field_query} WHERE {where_key} = '{where_val}' 
        """
        print(update_query)
        return self.__call_db(update_query)


if __name__ == "__main__":
    db1 = DB("Testing.db")
    db2 = DB("../Testing2.db")

    db2.insert(table="person", fields={"name": "Anton", "age": "20"})
   



