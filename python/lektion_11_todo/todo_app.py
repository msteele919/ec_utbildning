import requests 

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
    res = requests.post(url("/add_todo"))
    print(res.json())
    pass

def get_todo():
    print("get todo")
    res = requests.get(url("/todos"))
    print(res.json())
    pass

def delete_todo():
    print("Delete todo")
    res = requests.delete(url("/delete_todo/1"))
    print(res.json())
    pass

def update_todo():
    print("update todo")
    res = requests.put(url("/update_todo/1"))
    print(res.json())
    pass

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
            get_todo()
        case 3:
            delete_todo()
        case 4: 
            update_todo()
        case 5:
            exit()
        case _: # means default case    
            print("Please enter a valid choice")
            
    pass


while __name__ == "__main__":
    print(__name__)
    main() #__main__  sees which is main. and it makes sure that this is the main file. 



