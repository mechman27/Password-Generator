# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {
#     "A": "Alpha", "B": "Bravo", 
#     "C": "Charlie", "D": "Delta", 
#     "E": "Echo", "F": "Foxtrot", 
#     "G": "Golf", "H": "Hotßel", 
#     "I": "India", "J": "Juliet", 
#     "K": "Kilo", "L": "Lima", 
#     "M": "Mike", "N": "November", 
#     "O": "Oscar", "P": "Papa", 
#     "Q": "Quebec", "R": "Romeo", 
#     "S": "Sierra", "T": "Tango", 
#     "U": "Uniform", "V": "Victor", 
#     "W": "Whiskey", "X": "X-ray", 
#     "Y": "Yankee", "Z": "Zulu"}
import pandas

#this iterates through each row in the CSV file 
# and then creates a dictionary with the letter as the key and the phonetic code word as the value.
data = pandas.read_csv("Intermediate/Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#This accepts the user's input as a string, then splits the string into a list of letters
#and then uses those letters to pull the value from the dictionary, based off the key, being the letter.
word = input("Enter a word: ").upper()
split_word = [alpha_dict[letter] for letter in word]
print(split_word)