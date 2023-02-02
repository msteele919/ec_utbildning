
import sqlite3
from fastapi import FastAPI
# import uvicorn # få köra våra skript från lokal server 

# må behäver starta ett shell för att kunna komma åt uvicorn
#** pipenv shell **# 
#** sen skickaR uvicorn shell i terminalen 
# då kan vi skapa våran app genom FastAPI()

app = FastAPI() #initiera vår FASTAPI app # vi kommer att köra den här i uvicorn senare

def call_db(query: str, *args):
    connection = sqlite3.connect("api.db") 
    cursor = connection.cursor()
    res= cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit() 
    connection.close()
    return data

def populate_database():
    connection = sqlite3.connect("api.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY,  name VARCHAR(255) NOT NULL)"
    )
    cur.execute("INSERT INTO person (name) VALUES( 'Anton')")
    cur.execute("INSERT INTO person (name) VALUES( 'Karl')")
    cur.execute("INSERT INTO person (name) VALUES( 'Erik')")
    cur.close
    connection.commit()
    connection.close()
    pass

@app.get("/") # den här är en dekorator, så jag behöver en @
def root(): 
    return "Hello World"


@app.get("/populate")                   
def root(): 
    """
    this call kör den populate_database() functionen vilken skriver ut populated on the server
    But more importantly creates and populates a database 
    """ 
    populate_database()
    return "Populated"

@app.get("/people")                   
def get_people():
    person_query = """
    SELECT * FROM person
    """
    people = call_db(person_query)
    """
    go into our database and return every entry from the person column 
    """
    return people 

@app.get("/people/{id}")
def get_person_by_id(id:int):
    get_person_query = """
    SELECT * FROM person 
    WHERE id = ?
    """
    data = call_db(get_person_query, id) #här populera frågatecken
    return data
#nu har vi en api 

## efter det här kör vi i terminalen: 

# uvicorn vilken fil jag är i:och vad jag vill lköra för objekt 
# använd kommando --reload så att man inte behöver starta om hela tiden 

    # uvicorn first_api:app --reload

    # terminalen bör ser ut så här : 
    #     INFO:     Will watch for changes in these directories: ['/Users/mstee/Documents/GitHub/ec_utbildning/python/lektion_9']
    #     INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    #     INFO:     Started reloader process [4742] using StatReload
    #     INFO:     Started server process [4744]
    #     INFO:     Waiting for application startup.
    #     INFO:     Application startup complete.


# -> se att vi har startat en sever:    http://127.0.0.1:8000 (Press CTRL+C to quit)
    # man kan går till den i webbläsare och då ser man "hello world"
    # däremot kan man behöver spara först innan man går till webbsidan 


# skulle kunna göra en till för att demonstrera vad händer , dock fungerar den inte för mig än. 

@app.get("/test") # den här är en dekorator, så jag behöver en @
def test(): 
    print("This is my test place") # kommer att skrivas ut i terminalen
    return "Hello Test"


@app.get("/test/fisk/badnan") # använder vilken logik vi vill in våran funktion. 
def test2(): 
    i = 0 
    while True: 
        print("Hello World")
        i += 1 
        if i > 10: 
            break

    return "Hello Test, fisk, banan"