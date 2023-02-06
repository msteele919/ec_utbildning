from fastapi import FastAPI 
from pydantic import BaseModel

class Todo(BaseModel): #data class. You don't have to do an init method. 
    id: int = None
    title: str
    descript: str

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
def add_todo(todo: Todo):
    return "adds a task"

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    return "deletes a task with id: " + str(id)

@app.put("/update_todo/{id}")
def update_todo(id: int):
    return "Will update task with id: " + str(id)

