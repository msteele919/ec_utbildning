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
    medicin = input("Elevs medicin? Om inga medicin given skriv 'null':  ")
    nytidskapad = input("Har en ny tid bokats? Skriv True = ny tid bokad eller False = ingen ny tid bokad : ")
    ny_journal = Journaler(datum=datum, student_personnummer= student_personnummer , specialist= specialist , 
                           prognos= prognos , anteckningar= anteckningar , medicin= medicin , nytidskapad= nytidskapad)
    res = requests.post(url("/add_journal"), json = ny_journal.dict())
    print(res)

def hämta_journal(): 
    jounraler = []
    print("Hämta alla journaler")
    res = requests.get(url("/journaler"))
    if not res.status_code == 200: 
        return 
    data = res.json()
    for journal in data: 
        journal = Journaler(**journal)
        print("________")
        print(f"Journal id: {journal.journal_id}")
        print(f"Datum : {journal.datum}")
        print(f"Elevs personnummer : {journal.student_personnummer}")
        print(f"Specialists ID : {journal.specialist}")
        print(f"Elevs prognos : {journal.prognos}")
        print(f"Anteckningar : {journal.anteckningar}")
        print(f"Elevs medicin : {journal.medicin}")
        print(f"Nytidskapad : {journal.nytidskapad}")

def uppdatera_journal(journalerna: List[Journaler]): 
    print("Uppdatera en elevs journal", journalerna)
    journal_att_uppdatera = input("Journal ID av journalen som ska uppdateras: ")
    if not str.isdigit(journal_att_uppdatera):
        print("journal ID är en integer")
        return 
    
    index= None 
    for i, journal in enumerate(journalerna): 
        print(journal.journal_id)
        if journal.journal_id == int(journal_att_uppdatera): 
            index = i
            break 

    if index == None: 
        print("Ingen journal")
        return
    journal = journalerna[index]

    datum = input("Journal datum(lämna om det är samma): ")
    student_personnummer = ("Elevs personnummer (lämna om det är samma): ")
    specialist = input("Specialistensid (lämna om det är samma): ")
    prognos = input("Prognos enligt regionenskatalog (siffrakod) (lämna om det är samma): ")
    anteckningar = input("Specialistens anteckningar (lämna om det är samma): ")
    medicin = input("Elevs medicin? Om inga medicin given skriv 'null' (lämna om det är samma):  ")
    nytidskapad = input("Har en ny tid bokats? Skriv True = ny tid bokad eller False = ingen ny tid bokad  (lämna om det är samma): ")

    if not datum:
        datum = journal.datum
    if not student_personnummer:
        student_personnummer = journal.student_personnummer
    if not specialist:
        specialist= journal.specialist
    if not prognos:
        prognos = journal.prognos
    if not anteckningar:
        anteckningar = journal.anteckningar
    if not medicin:
        medicin = journal.medicin
    if not nytidskapad:
        nytidskapad = journal.nytidskapad

    ny_journal = Journaler(datum=datum, student_personnummer= student_personnummer , specialist= specialist , 
                           prognos= prognos , anteckningar= anteckningar , medicin= medicin , nytidskapad= nytidskapad)
    res = requests.put(url(f"/uppdatera_journal/{journal_att_uppdatera}"), json = ny_journal.dict())
    print(res.json())
def radera_journal():
    ("Du har valt radera journal. Ange lösenord för att kunna göra detta:")
    lösnord= input()
    if lösnord != 1234:
        print("Lösenord är fel")
        return
    journal_att_radera = input("Journal Id av journal du vill radera: ")
    if not str.isdigit(journal_att_radera):
        print("Ids är integer")
        return 
    res = requests.delete(url(f"/delete_journal/{journal_att_radera}"))
    print(res.json())    
    
    
    
    
    pass 


def main(): 
    print_menu()
    val = input("Vad vill du göra?: ")
    val = val.strip()
    if not str.isdigit(val):
        print("Välj ett val som finns")
        return 
    
    match int(val):
        case 1: 
            add_journal()
        case 2: 
            journalerna = hämta_journal()
        case 3: 
            journalerna = hämta_journal() 
            uppdatera_journal(journalerna)
        case 4: 
            radera_journal()
        case 5:
            exit()
        case _:
            print("Välj ett av val i listan") 

while __name__ == "__main__":
    main()






    