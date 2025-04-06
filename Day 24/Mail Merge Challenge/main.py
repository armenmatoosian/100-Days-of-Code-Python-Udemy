#TODO: Create a letter using starting_letter.txt
from pycodestyle import readlines

#for each name in invited_names.txt
with open("../Mail Merge Challenge/Input/Names/invited_names.txt", "r") as name_list:
    names = name_list.readlines()
#Replace the [name] placeholder with the actual name.
with open("../Mail Merge Challenge/Input/letters/starting_letter.txt", "r+") as letter_template:
    letter = letter_template.read()
    for name in names:
        final_letter = letter.replace("[name]", name.strip())
        # Save the letters in the folder "ReadyToSend".
        with open(f"../Mail Merge Challenge/Output/ReadyToSend/{name.strip()}.txt", "w") as ready_to_send_letter:
            ready_to_send_letter.write(final_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp