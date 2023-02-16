import json 
from db_1 import DB 

db = DB("elevhälsa.db")
create_elev = """
INSERT INTO elev (
personnummer,
efternamn,
förstanamn,
ålder,
grundskola
) VALUES (
?, ?, ?, ?, ?
);
"""

create_journal = """
INSERT INTO journal (
datum,
student_personnummer,
specialist,
prognos,
anteckningar,
medicin,
nytidskapad
) VALUES (
?, ?, ?, ?, ?, ?, ?
)
"""

create_specialist = """
INSERT INTO specialist (
id_specialist,
efternamn,
förstanamn,
titel,
specialisering
) VALUES (
?, ?, ?, ?, ?
)
"""

with open("seed_elevhälsa.json", "r") as seed:
    data = json.load(seed)

    for elev in data["elever"]:
        db.call_db(create_elev, elev["personnummer"], elev["efternamn"], elev["förstanamn"], elev["ålder"], elev["grundskola"])

    for journal in data["journaler"]:
        db.call_db(create_journal, journal["datum"], journal["student_personnummer"], journal["specialist"], journal["prognos"], 
                   journal["anteckningar"], journal["medicin"], journal["nytidskapad"])

    for specialist in data["specialister"]:
        db.call_db(create_specialist, specialist["id_specialist"], specialist["efternamn"], specialist["förstanamn"], specialist["titel"], specialist["specialisering"])

    
