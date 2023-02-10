from typing import List
import requests 
from api import Todo
def url(route:str):
    return f"http://127.0.0.1:8000{route}"

def print_menu():
    print("""
    1: add_todo()
    2: get_todo()
    3: delete_todo()
    4: update_todo()
    5: exit()
    """)
    pass

def add_todo():
    print("Add todo")
    title = input("Todo title: ")
    descript = input("Todo description: " ) 
    new_todo = Todo(title=title, descript = descript)
    res = requests.post(url("/add_todo"), json = new_todo.dict())
    print(res)
    

def get_todo():
    todos = []
    print("get todo")
    res = requests.get(url("/todos"))
    if not res.status_code == 200: 
        return
    data = res.json()
    for todo in data:
        todo = Todo(**todo) # är lika med = Todo["title"], descript = todo["descript"]
        print("_________")
        print(f"ID:      {todo.id}")
        print(f"Title:   {todo.title}")
        print(f"Details: {todo.descript}")
        todos.append(todo)
    return todos
    

def delete_todo():
    print("Delete todo")
    todo_to_delete = input("Id of todo you wish to delete: ")
    if not str.isdigit(todo_to_delete):
        print("Ids are not integers")
        return
    res = requests.delete(url(f"/delete_todo/{todo_to_delete}"))
    print(res.json())
    

def update_todo(todos: List[Todo]):
    print("update todo")
    
    todo_to_update= input("Id of todo you wish to update: ")
    if not str.isdigit(todo_to_update):
        print("Ids are not integers")
        return
    
    index = None
    for i, todo in enumerate(todos):
        if todo.id == int(todo_to_update):
            index = i 
            break

    if index  == None: 
        print("No such todo")
        return
    todo = todos[index]

    title = input("Todo title (leave blank if same ): ")
    descript = input("Todo description ( leave blank if same): ") 

    if not title: 
        title = todo.title 
    if not descript: 
        descript = todo.descript

    new_todo  = Todo(title = title, descript = descript)
    res = requests.put(url(f"/update_todo/{todo_to_update}"), json = new_todo.dict())
    print(res.json())
   

def main():
    print_menu()
    choice = input("PLease choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice): # alternativ till en if sats 
        print("Please enter a valid option: ")
        return
    
    match int(choice): # match är ny i python. it's an alternative to an if, elif elif elif else
        case 1: 
            add_todo()
        case 2:
            todos = get_todo()
        case 3:
            delete_todo()
        case 4: 
            todos = get_todo()
            update_todo(todos)
        case 5:
            exit()
        case _: # means default case    
            print("Please enter a valid choice")
            
    pass


while __name__ == "__main__":
    print(__name__)
    main() #__main__  sees which is main. and it makes sure that this is the main file. 



