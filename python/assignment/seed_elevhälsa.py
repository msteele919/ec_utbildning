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
INSERT INTO journaler (
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

    for journaler in data["journaler"]:
        db.call_db(create_journal, journaler["datum"], journaler["student_personnummer"], journaler["specialist"], journaler["prognos"], 
                   journaler["anteckningar"], journaler["medicin"], journaler["nytidskapad"])

    for specialist in data["specialister"]:
        db.call_db(create_specialist, specialist["id_specialist"], specialist["efternamn"], specialist["förstanamn"], specialist["titel"], specialist["specialisering"])

    
