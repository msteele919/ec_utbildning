from typing import List
from fastapi import FastAPI 
from pydantic import BaseModel

class Todo(BaseModel): #data class. You don't have to do an init method. 
    id: int = None
    title: str
    descript: str

app = FastAPI()
app.curr_id = 1

# app["todos"] : List[Todo]
app.todos : List[Todo] = []

@app.get("/") # @ är en dekorator- den ändra beteendet på nästa funktion 
def root(): 
    return "Hello and welcome to Michaels todos"

@app.get("/todos")
def get_todos():
    return app.todos 

@app.get("/todo/{id}")
def get_todo(id: int):
    return "returns a single todo item" + str(id)  # make sur ethis is a formated string. Not by itself: id 

@app.post("/add_todo")
def add_todo(todo: Todo):
    print(todo)
    todo.id = app.curr_id
    app.todos.append(todo)
    app.curr_id += 1 
    return "adds a task"

@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    app.todos = list(filter(lambda todo: todo.id != id, app.todos)) #lambda är en funktion. 
    return True 
    # return "deletes a task with id: " + str(id)

@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):
    for todo in app.todos:
        if todo.id == id: 
            todo.title = new_todo.title
            todo.descript = new_todo.descript

    return "Will update task with id: " + str(id)

