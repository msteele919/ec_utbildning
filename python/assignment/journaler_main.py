# from dotenv import load_dotenv 

# load_dotenv() # didnt install. dont know if its necessary 
from collections import Counter
import csv 
import os 
from typing import List 
import requests 
from api_1 import Journaler
import pandas as pd

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
    3. Hämta en journal
    4. Uppdatera en journal
    5. Radera en journal
    6. Skriv en csvfil med databasen
    7. Lämna verktyget
    """
    )
    pass 
    
def add_journal():
    print("Lägga till en journal")
    datum = input("Journal datum: ")
    student_personnummer = input("Elevs personnummer: ")
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
    journaler = []
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
        journaler.append(journal)
    return journaler

def skriv_csv(journaler, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['journal_id', 'datum', 'student_personnummer', 'specialist', 'prognos', 'anteckningar', 'medicin', 'nytidskapad']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for journal in journaler:
            writer.writerow({'journal_id': journal.journal_id,
                             'datum': journal.datum,
                             'student_personnummer': journal.student_personnummer,
                             'specialist': journal.specialist,
                             'prognos': journal.prognos,
                             'anteckningar': journal.anteckningar,
                             'medicin': journal.medicin,
                             'nytidskapad': journal.nytidskapad})
    
    print(f"{filename} created sucessfully")

def hämta_en_journal():
    # journal = []
    print("hämta en journal")
    journal_att_hämta = input("Ange journal ID från journal du vill ha: ")
    if not str.isdigit(journal_att_hämta):
        print("journal ID är en integer")
        return 
    res = requests.get(url(f"/journal/{journal_att_hämta}"))
    if not res.status_code == 200: 
        return
    print(res.json())
    

def uppdatera_journal(journaler: List[Journaler]): 
    print("Uppdatera en elevs journal", journaler)
    journal_att_uppdatera = input("Journal ID av journalen som ska uppdateras: ").strip()
    if not str.isdigit(journal_att_uppdatera):
        print("journal ID är en integer")
        return 
    
    index= None 
    for i, journal in enumerate(journaler): 
        # print(journal.journal_id)
        if journal.journal_id == int(journal_att_uppdatera): 
            index = i
            break 

    if index == None: 
        print("Ingen journal")
        return
    journal = journaler[index]

    datum = input("Journal datum(lämna om det är samma): ")
    student_personnummer = input("Elevs personnummer (lämna om det är samma): ")
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

    ny_journal = Journaler(datum=datum, student_personnummer= student_personnummer, specialist= specialist, 
                           prognos= prognos, anteckningar= anteckningar, medicin= medicin, nytidskapad= nytidskapad)
    res = requests.put(url(f"/update_journal/{journal_att_uppdatera}"), json = ny_journal.dict())
    if not res.status_code == 200: 
        return 
    print(res.json())


def radera_journal():
    # print("Du har valt radera journal. Ange lösenord för att kunna göra detta:")
    lösnord= int(input("Du har valt radera journal. Ange lösenord för att kunna göra detta:"))
    if lösnord !=1234:
        print("Lösenord är fel")
        return
    journal_att_radera = input("Journal Id av journal du vill radera: ")
    if not str.isdigit(journal_att_radera):
        print("Ids är integer")
        return 
    res = requests.delete(url(f"/delete_journal/{journal_att_radera}"))
    if not res.status_code == 200: 
        return 
    print(res.json())    
def write_csv(journaler):
    journaler = journaler["items"]
    journaler_df = pd.DataFrame(journaler)
    return journaler_df.to_csv("csv.csv")



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
            journalar = hämta_journal()
        case 3:
            hämta_en_journal()
        case 4: 
            journalar = hämta_journal() 
            uppdatera_journal(journalar)
        case 5: 
            radera_journal()
        case 6:
            journaler = hämta_journal()
            skriv_csv(journaler, 'journaler.csv')
        case 7:
            exit()
        case 8:
            journaler = hämta_journal()
            write_csv(journaler)
        case _:
            print("Välj ett av val i listan") 

while __name__ == "__main__":
    main()






    