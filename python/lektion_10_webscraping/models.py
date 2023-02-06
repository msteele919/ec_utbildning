from pydantic import BaseModel #eftersom vi använder fast api har vi fastapi 


class Person(BaseModel): #adding (BaseModel) är att extenda 
    name:str
    title: str
    mail: str
    tel: str 
