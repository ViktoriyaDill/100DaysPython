#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_of_name = names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as txt:
    txt = txt.read()

for name in list_of_name:
    new_text = txt.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invited:
        invited.write(new_text)





