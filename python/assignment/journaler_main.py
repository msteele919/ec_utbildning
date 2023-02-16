# from dotenv import load_dotenv 

# load_dotenv() # didnt install. dont know if its necessary 
import os 
from typing import List 
import requests 
from api_1 import Journaler

DB_URL = os.getenv("DB_URL", "http://127.0.0.1:8000")

def url(route: str):
    return f"{DB_URL}{route}"

print("""Välkommen till journaler app. Här få du tillgång till alla journaler i region XX

Här får du: hitta alla journaler, hitta en journal med en journal id, lägga till journaler, radera journaler och uppdatera journaler
""")
      
def print_menu():
    print( 
        """
    1. Lägga till en journal
    2. Hämta alla journaler
    3. Uppdatera en journal
    4. Radera en journal
    """
    )
    
def add_journal():
    print("Lägga till en journal")
    datum = input("Journal datum: ")
    student_personnummer = ("Elevs personnummer: ")
    specialist = input("Specialistensid: ")
    prognos = input("Prognos enligt regionenskatalog (siffrakod): ")
    anteckningar = input("Specialistens anteckningar: ")
    medicin = input("Namnet på medicin given? Om inga medicin given skriv null:  ")
    nytidskapad = input("Har en ny tid bokats? Skriv True = ny tid bokad eller False = ingen ny tid bokad : ")
    ny_journal = Journaler(datum=datum, student_personnummer= student_personnummer , specialist= specialist , 
                           prognos= prognos , anteckningar= anteckningar , medicin= medicin , nytidskapad= nytidskapad)
    
    





    