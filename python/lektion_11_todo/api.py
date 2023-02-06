from fastapi import FastAPI 

app = FastAPI()

@app.get("/") # @ är en dekorator- den ändra beteendet på nästa funktion 
def root(): 
    return "Hello and welcome to Michaels todos"

@app.get("/todos")
def get_todos():
    return "Returns a list of todos"

@app.get("/todo/{id}")
def get_todo(id: int):
    return "returns a single todo item" + str(id)  # make sur ethis is a formated string. Not by itself: id 

@app.post("/add_todo")
def add_todo(todo):
    return "adds a task"

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    return "deletes a task with id: " + str(id)

@app.put("/update_todo/{id}")
def update_todo(id: int):
    return "Will update task with id: " + str(id)

