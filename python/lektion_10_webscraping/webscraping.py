import json
from dataclasses import dataclass
import re
from typing import List 
import requests 
from bs4 import BeautifulSoup

from models import Person #använde models and base model instead of creating the class directly in the file. 

# @dataclass
# class Person:
#     name:str
#     title: str
#     mail: str
#     tel: str 


##kommer att skrapa ec utbildnings webbsida och skrapa namn/kontaktinformation från studieledare

api_url = "http://127.0.0.1:8000" 
url = "https://ecutbildning.se/utbildningar/data-scientist/"

res = requests.get(url)

page = res.text
print(page)

soup = BeautifulSoup(page, "html.parser") #måste identifiera våran parser

print(soup.prettify()) #använd prettify för att formatera json

title= soup.find("title").text #krivas ut det som finns på tabben. i detta fallet: Data Scientist | Yh-utbildning dataanalytiker | EC Utbildning

heading = soup.find("h1").text #få Data Science. .text ge texten inom htmln 

headings = soup.find_all("h2")

# print(title)
# print(heading)
# print(headings)

# ##skriv ut alla headings
# for element in headings: 
#     print(element.text)


# p_tags = soup.find_all("p")

# for tag in p_tags: 
#     # print(tag)
#     test = tag.find("em")
#     print(test)


# test = soup.find_all(string=re.compile("Molly")) #Look to see if "molly" is in a text. Få ['Molly Tagesson']
# print(test)

#"resultatet vi vill ha, men inte förtjänar 

# cards = soup.find_all("article", class_="card")
# print(cards)


#kolla efter alla a_tagar som har "mailto" eller "tel"
a_tags = soup.find_all("a")

people_soup = []
for tag in a_tags:
    if tag.has_attr("href"):
        if "mailto" in tag["href"]:
            if "card-body" in tag.parent.parent.parent["class"]:
                tag = tag.parent.parent.parent
                people_soup.append(tag)

            

print(people_soup)

people: List[Person] = []
for person in people_soup:
    print("___")
    # print(person.prettify())
    name = person.find("h3").text
    title = person.find("p", itemprop = "jobTitle").text.strip()
    tel = ""
    phone = ""
    person_links= person.find_all("a") #både telefon och mejl itemprop = "telephone". Måste iteratera över dem. 
    # print(person_links)
    for link in person_links: 
            if link["href"].startswith("tel"):
                phone = link.text.strip()
            elif link["href"].startswith("mailto"):
                mail= link.text.strip()

    people.append(Person(name=name, title=title, mail=mail, tel= phone)) # måste använde key word arguments med pydantic istället för Person(name, title, mail, phone)
    # print(name)
    # print(title)


for person in people: 
    requests.post(api_url + "/create_person", json.dumps(person.__dict__))

## nu ska vi skapa en api som kan skicka denna data 