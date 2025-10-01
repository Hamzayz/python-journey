# Errors , Exceptions and Saving JSON data :

# File not found Error :
# with open("text.txt") as file:
    # file.read()

    
# keyError:
# dictonary = {"name" : "hamza"
#             "class" :"1st year"
# }
# dictonary["age"]

# IndexError :
# list = ["apple","banana","orange"]
# print(list[3])

# TypeError :
# text = "abc"
# text + 5

# reduce the error with Exceptions
# try:
#     file = open("hamza.txt")
#     dictonary = {"key":"value"}
#     print(dictonary["hamza"])
# except FileNotFoundError: # always write the error name its is vary usefull an if you dont write it will have an error
#     file = open("hamza.txt" , "w")
#     file.write("everything")
# except KeyError as errormessage: # errormessage will give the key which is giving an error
#     print(f"there is no {errormessage} key")

# else: # if try bolck has no error then this block will excute
#     file.read()

# finally: # no matter the code has error or not it will excute
#     file.close()
#     raise ValueError # we can raise our own errors 

height = int(input("what is your hight"))
weight = int(input("what is your weight"))

if height > 3 :
    raise ValueError ("Human height can not be grater than 3 meters")

bmi = weight / height**2
print(bmi)