import sqlite3 # behöver inte installera biblioteken


# #skapa en hotlink till en database, det finns inte än, (men man får gör det ändå)

# connection = sqlite3.connect("test.db")  #om databasen inte finns, kommer den att skapas. Finns den redan, då kopplas den

# cursor = connection.cursor() #peka på en rad i db för att kunna göra någonting 

# #vad kan man göra med cursor? börja skapa sakar i databas med SQL! 

# # create tables 

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name VARCHAR(80));"
#     ) # create a table

# # cursor.execute(
# #    "CREATE TABLE IF NOT EXISTS test2 (id INTEGER PRIMARY KEY, name VARCHAR(80));"
# #    ) # create a second table

# #insert values into tables 

# #cursor.execute("INSERT INTO test (name) VALUES ('camille')") #enter data into a table. Note that connection.commit() is needed to insert data. 
# #cursor.execute("INSERT INTO test (name) VALUES ('michael')")
# #cursor.execute("INSERT INTO test (name) VALUES ('stina')")
# #cursor.execute("INSERT INTO test (name) VALUES ('jakob')")
# # insert values using multilines

# """cursor.execute(
#     "CREATE TABLE IF NOT EXISTS test3 (id INTEGER PRIMARY KEY, name VARCHAR(80));"
#     ) # create a third table
# """
# person_query = """
# INSERT INTO test(
#     name 
# ) VALUES (
#     'Tove'
# )
# """
# cursor.execute(person_query)

# res = cursor.execute(
#     "SELECT name FROM test") # use FROM sqlite_master if you want everything from the entire database 


# data = res.fetchone() # fetchone returnera det första objektet. 
# print(data)
# data = res.fetchone()
# print(data)
# # data2 = res.fetchall() # returnära allt från db, table1, table2, table3

# # cursor.execute("DROP TABLE test2;")
# # cursor.execute("DROP TABLE test3;")

# # print(data)
# #print(data2)

# cursor.close()
# connection.commit() 
# connection.close() # Man ska stänga databasen efteråt


############################
#Make a function to make creaing a function a bit more reusable 
############################


def call_db(query, *args):
    connection = sqlite3.connect("test.db") 
    cursor = connection.cursor()
    res= cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit() 
    cursor.close()
    return data

# query = """
# INSERT INTO person (
#     first_name,
#     last_name,
#     motto
# ) VALUES (
#     ?, ?, ?
# )
# """
# data = call_db(query, "Jack", "Sparrow", "Drink and be merry!")
# print(data)

# query = """
# CREATE TABLE IF NOT EXISTS person (
#     id INTEGER PRIMARY KEY,
#     first_name VARCHAR(80),
#     last_name VARCHAR(80),
#     motto VARCHAR(255)
#     )
# """

# data = call_db(query)  
# print(data)

# query = """
# INSERT INTO person(
#     first_name,
#     last_name,
#     motto
# ) VALUES (
#     "Michael",
#     "Steele",
#     "Live life!"
# )
# """
# data = call_db(query)  
# print(data)

# query= """
# SELECT * FROM person
# WHERE first_name = 'Michael'
# """
# data = call_db(query)  
# print(data)
