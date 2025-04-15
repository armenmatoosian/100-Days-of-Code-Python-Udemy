student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#my code for NATO Alphabet project
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_alphabet_dict = {row.letter:row.code for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = list(input("Enter a word: ").upper())
#my code - not in order
# user_word_to_nato_alphabet = [nato_letter for (letter, nato_letter) in nato_alphabet_dict.items() if letter in user_word]
#solution code - in order
user_word_to_nato_alphabet = [nato_alphabet_dict[letter] for letter in user_word]
print(user_word_to_nato_alphabet) #could not get this to print in order