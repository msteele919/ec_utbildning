from fastapi import FastAPI 
from models import Person 
from db import DB 
# pipenv install fastapi uvicorn # i den ordning 

app = FastAPI()
db= DB ("people.db")


@app.get('/')
def root():
    return "hello"

@app.get("/people")
def get_people():
    get_people_query = """
    SELECT * FROM people
    """
    data = db.call_db(get_people_query)
    return data 

@app.get("/people/{id}")
def get_people_by_id(id: int):
    get_people_by_id_query = """
    SELELCT * FROM people
    WHERE id = ? 
    """
    data = db.call_db(get_people_by_id_query, id)
    return data 

@app.post("/create_person")
def create_person(person: Person):
    create_person_query = """
    INSERT INTO people(
        name, title, mail, tel
    ) VALUES (
        ?, ?, ?, ?
    )
    """
    db.call_db(create_person_query, person.name, person.title, person.mail, person.tel)
    return person