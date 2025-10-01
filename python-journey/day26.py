# Day 26 :
# list and dictionary comprahinsion

# List Comprehension :
# it replace fore loop and write it in simple and short way
# i.e new_list = [new_list for item in list]

# new_list means we want to add some thing to the previous list like n+1
# item is the name that we write in for loop too it can be anything
# list is the previous list that we want to change

# i.e new_list = [new_list for item in list if test]
# you can also add the condition 

# Dictionary Comprehension :
# we can make new dictioney from list
# i.e new_dictionary = {new_key : new_value for item in list}
# making dictionary from another dictionary
# i.e new_dictionary = {new_key : new_value for item in dict.item}
# i.e new_dictionary = {new_key : new value for item in dict.item if test}f

# loop through pandas
# i.e new_dect{new_key : value_key for (index , row) in dc.iterrows}

import pandas as pd
student_scores = {
    "students": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"],
    "score": [65, 72, 45, 85, 90, 59]
}
students = pd.DataFrame.from_dict(student_scores)
print(students)
for index , row in students.iterrows():
    if row.students == "Alice":
        print(row.score)