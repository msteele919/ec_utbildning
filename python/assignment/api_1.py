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
    journal_id: int
    datum: str #assuming str eftersom den kommer innahålla '/' och sånt 
    student_personnummer: int 
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
        datum, student_personnummer, specialist, prognos, anteckningar, medicin, nytidskapad = element
        journalerna.append(Journaler(datum= datum, student_personnummer=student_personnummer, 
                                     specialist=specialist , prognos=prognos, anteckningar=anteckningar, medicin=medicin, 
                                     nytidskapad=nytidskapad))
    print(data)
    return journalerna
@app.get("/journal/{journal_id}")
def get_journal(journal_id: int): 
    return "Returnera en journal med journal_id: " + str(journal_id)

@app.post("/add_journal")
def add_journal(journal: Journaler):
    insert_query= """
    INSERT INTO journaler (datum, student_personnummer, specialist, prognos, anteckningar, medicin, nytidskapad)
    VALUES ( ?, ?, ?, ?, ?, ?, ? )
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
    return True 

@app.put("/update_journal/{journal_id]}")
def uppdatera_todo(journal_id: int, ny_journal: Journaler):
    uppdatera_todo_query = """
    UPDATE journaler
    SET datum = ?, student_personnummer = ?, specialist = ?, prognos = ?, anteckningar = ?, medicin = ?, nytidskapad = ?
    WHERE id = ?
    """
    db.call_db(uppdatera_todo_query, ny_journal.datum, ny_journal.student_personnummer, ny_journal.specialist,
                ny_journal.prognos, ny_journal.anteckningar, ny_journal.medicin, ny_journal.nytidskapad, journal_id)
    
    return True

# app.curr_id = 1 # * do I make a 1 for the first table, and so on. or should I use the same for all 
# app.elever: List[Elev]= []

# app.curr_id = 3 # * do I make a 1 for the first table, and so on. or should I use the same for all 
# app.specialister: List[Specialist]= []




    
