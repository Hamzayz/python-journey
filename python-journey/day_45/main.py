# type:ignore
from turtle import heading
from bs4 import BeautifulSoup
import lxml

with open("day-45/website.html") as file:
    content = file.read()

soup = BeautifulSoup(content , "html.parser")
# print(soup.title.string) 
# print(soup.h1.string) #gives first h1

all_ancor_tag = (soup.find_all(name="a")) # it will find all the a or p or h what you want

# for tag in all_ancor_tag:
#     print(tag.get_text()) # it will give you only text
#     print(tag.get("href")) # it will give you link 

heading = soup.find(name="h1" , id="name") #finding by id
# print(heading.get_text())

heading3 = soup.find(name="h3" , class_="heading")
# print(heading3.get("class")) # getting the contect or class or id or other thing by class_

link = soup.select_one(selector="p a") # i can also get the thing by giving id(#) or class
print(link) # it will give me the specific thing what i want