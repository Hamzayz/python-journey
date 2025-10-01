# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# converting file in to dictionary:
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato-26/nato_phonetic_alphabet.csv")

# Make a dictionary with student names as keys and scores as values
# result = data.set_index('letter')['code'].to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print("Welcome to the NATO Game")
# convert data to dictionary:
def letters():
    try:
        word = input("Enter the word: ").upper()
        phonetic_dict = {row.letter : row.code for (_ , row) in data.iterrows()}
        # prints values from dictionary:
        list = [phonetic_dict[letter] for letter in word]
        # print(list)
    except KeyError:
        print("Sorry only letters in the alphabits")
        letters()
    else:
        print(list)
letters()