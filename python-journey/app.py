from flask import Flask
import random

# app = Flask(__name__)

# def make_bold(func):
#   def wraping():
#     return "<b>" + func() + "</b>"
#   return wraping

# def make_empesis(func):
#   def wraping():
#     return "<em>" + func() + "</em>"
#   return wraping

# def make_underlined(func):
#   def wraping():
#     return "<u>" + func() + "</u>"
#   return wraping

# @app.route("/")
# @make_bold
# @make_empesis
# @make_underlined
# def hello_world():
#     return '<p>Hello World!<p>'
            

# @app.route("/<name>")
# def greet(name):
#   return f"hello {name}"

# # the __name__ is the name given to the module
# # the __main__ means the module __name__ is runible it can be accuited
# if __name__ == "__main__": 
#     app.run(debug=True)

# Project :
app = Flask(__name__)
random_num = random.randint(0, 9)
@app.route("/")
def home():
  return "<h1>Guess the number between 0 and 9</h1>"\
  "<img src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3eTRvYmxjbng2eWJoeTY1MTlqMmhxaXQyY3luMHN6YTRhZGRudmljdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nORl2l7PN8YDxCLaoA/giphy.gif'>"
@app.route(f"/<int:number>")
def right(number):
  if number == random_num:
    return "<h1 'style=colour:green'>You found me</h1>"\
    "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2RlcHZ3MjR5MnRjOW00ODJ1ZmtsMnVuY2FhbjFleTMxdHVhb2ExaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xDd7UQJcd3Z16FZqvu/giphy.gif'>"
  elif number > random_num:
    return "<h1 'style=colour:red'>Too high, guess again<h1>" \
      "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWV4c3Qxcmlxcm91cWR3Z2V6YnNwcnRqNXN6cjBwbml5a3BqZ2VjZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PLPcQzjESyGuNKNFrs/giphy.gif'>"
  elif number < random_num:
    return "<h1 'style=colour:red'>Too low, guess again<h1>"\
    "<img src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3eTRvYmxjbng2eWJoeTY1MTlqMmhxaXQyY3luMHN6YTRhZGRudmljdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KGwQnsUVRmAXlVP5b8/giphy.gif'>"

if __name__ == "__main__":
  app.run(debug=True)

