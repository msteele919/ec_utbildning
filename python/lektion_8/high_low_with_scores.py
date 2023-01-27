#################
# An example of how you can call a function from another file
# In this example we are using the call_db funcdtion to create a db 
# from the results of this game 
#################

#################
# ***Instructions on how to use call_db in this function**
# 1st. need to have a data base to hold the results, the high scores
#      so we create a table with the results 
# 2nd. want to call the call_db function to 
        # def call_db(query:str):
        #     connection = sqlite3.connect("test.db") 
        #     cursor = connection.cursor()
        #     res= cursor.execute(query)
        #     data = res.fetchall()
        #     cursor.close()
        #     connection.commit() 
        #     cursor.close()
        #     return data
# 3rd. Want to query the table to see if we got any results 
#################



import random
from sql_lite import call_db

###***####
create_highscores_table = """
CREATE TABLE IF NOT EXISTS high_scores (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL
)
"""
get_highscore_query = """
SELECT name, score FROM high_scores
"""

save_score_query = f"""
        INSERT INTO high_scores (
            name,
            score
        ) VALUES (
            ?,
            ?
        )
        """
# / QUERIES 

call_db(create_highscores_table) #call the function to actually make the table

max = 10
min = 1

score = 0

##******####
random_num = random.randint(min, max) # Returnerar en string
highscores = call_db(get_highscore_query)

def print_highscore():
    print("_____HIGHSCORES_____")
    for highscore in highscores:
        name, score = highscore 
        print(f"{name}: {score}")
    print("_____HIGHSCORES_____")

print_highscore() 

while True:
    print("Ditt nummer är: ", random_num)

    guess = input("Vad är din gissning högre eller lägre? (h/l) (exit): ")

    if guess != "h" and guess != "l" and guess != "exit":
        continue

    if guess == "exit":
        print("Tack för att du spelade")
        break

    new_num = random.randint(min, max)

    if new_num >= random_num and guess == "h":
        score += 1
        print("Rätt, din score är: ", score)
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Rätt, din score är: ", score)
    else:
        print("Fel din score var: ", score)
        name = input("Skriv in ditt name: ")
        # save_score_query = f"""
        # INSERT INTO high_scores (
        #     name,
        #     score
        # ) VALUES (
        #     '{name}',
        #     '{score}'
        # )
        # """
        call_db(save_score_query, name, score)
        score = 0
        print("Prova igen")
        print_highscore()

    random_num = new_num