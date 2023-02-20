import os 
from typing import List 
import requests 
from api_1 import Specialist


DB_URL = os.getenv("DB_URL", "http://127.0.0.1:8000")


def url(route: str):
    return f"{DB_URL}{route}"


 
def print_menu():
    print( 
        """
    1. Lägga till en specialist
    2. Hämta alla journaler
    3. Hämta en journal
    4. Uppdatera en journal
    5. Radera en journal
    6. Lämna verktyget
    """
    )



def add_specialist():
    print("Lägga till en specialist i systemet")
    id_specialist = input("Specialistens ID: ")
    efternamn = input("Specialistens efternamn: ")
    förstanamn = input("Specialistens förstanamn: ")
    titel = input("Vilken titel har specialisten: ")
    specialisering = input("specialisering: ")
    ny_specialist = Specialist(id_specialist=id_specialist, efternamn= efternamn, förstanamn= förstanamn, 
                           titel= titel, specialisering= specialisering)
    res = requests.post(url("/add_specialist"), json = ny_specialist.dict())
    print(res)


def radera_specialist():
    specialist_att_radera = input("Id av specialist du vill radera från systemet: ")
    if not str(specialist_att_radera):
        print("Ids är sträng")
        return 
    res = requests.delete(url(f"/delete_specialisten/{specialist_att_radera}"))
    if not res.status_code == 200: 
        return 
    print(res.json())  

def main(): 
    print_menu()
    val = input("Vad vill du göra?: ")
    val = val.strip()
    if not str.isdigit(val):
        print("Välj ett val som finns")
        return 
    
    match int(val):
        case 1: 
            add_specialist()
        case 2:
            radera_specialist()
        case 3:
            exit()
        case _:
            print("Välj ett av val i listan") 

while __name__ == "__main__":
    main()