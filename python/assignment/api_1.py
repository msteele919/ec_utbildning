from typing import List 
from fastapi import FastAPI 
from pydantic import BaseModel

from db_1 import DB 

class Elev(BaseModel): 
    personnumer: str 
    efternamn: str
    förstanamn: str 
    ålder: str 
    grundskola: str

class Journaler(BaseModel):
    journal_id: int = None
    datum: str #assuming str eftersom den kommer innahålla '/' och sånt 
    student_personnummer: str 
    specialist: str 
    prognos: int
    anteckningar: str 
    medicin: str 
    nytidskapad: bool
    pass

class Specialist(BaseModel): 
    id_specialist: str 
    efternamn: str 
    förstanamn: str 
    titel: str 
    specialisering: str
    pass

app = FastAPI()
db = DB("elevhälsa.db")

app.curr_id = 1 # * do I make a 1 for the first table, and so on. or should I use the same for all 
app.journalerna: List[Journaler]= []

### Journaler ###

@app.get("/")
def root():
    return "Hej och välkommen till elevhälsans journalsidan. Här kan du som specialist, rektor eller beslutsfattar få tillgång till XX regions psykiskhälsajournaler."

@app.get("/journaler")
def get_journaler():
    get_journaler_query = """
    SELECT * FROM journaler
    """
    data = db.call_db(get_journaler_query)
    journalerna= []
    for element in data: 
        journal_id, datum, student_personnummer, specialist, prognos, anteckningar, medicin, nytidskapad = element
        journalerna.append(Journaler(journal_id= journal_id,datum= datum, student_personnummer=student_personnummer, 
                                     specialist=specialist , prognos=prognos, anteckningar=anteckningar, medicin=medicin, 
                                     nytidskapad=nytidskapad))
    print(data)
    return journalerna
@app.get("/journal/{journal_id}")
def get_journal(journal_id: int): 
    get_journal_query = """
    SELECT * FROM journaler
    WHERE journal_id = ?
    """
    query = db.call_db(get_journal_query, journal_id)
    # data = db.call_db(get_journal_query, journal_id)
    # journal = []
    # for element in data: 
    #     journal_id, datum, student_personnummer, specialist, prognos, anteckningar, medicin, nytidskapad = element
    #     journal.append(Journaler(journal_id=journal_id, datum= datum, student_personnummer=student_personnummer, 
    #                                  specialist=specialist , prognos=prognos, anteckningar=anteckningar, medicin=medicin, 
    #                                  nytidskapad=nytidskapad))
    return query
    # return "Returnera en journal med journal_id: " + str(journal_id) + print(query) 

@app.post("/add_journal")
def add_journal(journal: Journaler):
    insert_query= """
    INSERT INTO journaler (datum, student_personnummer, specialist, prognos, anteckningar, medicin, nytidskapad)
    VALUES ( ?, ?, ?, ?, ?, ?, ?)
    """
    db.call_db(insert_query, journal.datum, journal.student_personnummer, journal.specialist, journal.prognos, journal.anteckningar,
                journal.medicin, journal.nytidskapad)
    
    return "Lägga till en ny journal"


@app.delete("/delete_journal/{journal_id}")
def delete_journal(journal_id: int): 
    delete_query = """
    DELETE FROM journaler WHERE journal_id = ? 
    """
    db.call_db(delete_query, journal_id)
    return "Journal deleted" 

@app.put("/update_journal/{journal_id}")
def uppdatera_journal(journal_id: int, ny_journal: Journaler):
    uppdatera_journal_query = """
    UPDATE journaler
    SET datum = ?, student_personnummer = ?, specialist = ?, prognos = ?, anteckningar = ?, medicin = ?, nytidskapad = ?
    WHERE journal_id = ?
    """
    db.call_db(uppdatera_journal_query, ny_journal.datum, ny_journal.student_personnummer, ny_journal.specialist,
                ny_journal.prognos, ny_journal.anteckningar, ny_journal.medicin, ny_journal.nytidskapad, journal_id)
    
    return True


app.curr_id = 2 # * do I make a 1 for the first table, and so on. or should I use the same for all 
app.specialister: List[Specialist]= []


@app.post("/add_specialist")
def add_specialist(specialist: Specialist):
    insert_query= """
    INSERT INTO specialist (id_specialist, efternamn, förstanamn, titel, specialisering)
    VALUES ( ?, ?, ?, ?, ?)
    """
    db.call_db(insert_query, specialist.id_specialist, specialist.efternamn, specialist.förstanamn, specialist.titel, specialist.specialisering)
    
    return "Lägga till en ny specialist i systemet"

@app.delete("/delete_specialisten/{id_specialist}")
def delete_specialisten(id_specialist: str): 
    delete_query = """
    DELETE FROM specialist WHERE id_specialist = ? 
    """
    db.call_db(delete_query, id_specialist)
    return "Specialist deleted" 
# app.curr_id = 1 # * do I make a 1 for the first table, and so on. or should I use the same for all 
# app.elever: List[Elev]= []






    
