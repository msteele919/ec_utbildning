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

    pass
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