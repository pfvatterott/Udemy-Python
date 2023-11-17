#TODO: Create a letter using starting_letter.txt 
letter_template = ""
with open("Section24FilesDirectoriesAndPaths\MailMerge\Input\Letters\starting_letter.txt") as file:
    content = file.read()
    letter_template = content
#for each name in invited_names.txt
name_array = []
with open("Section24FilesDirectoriesAndPaths\MailMerge\Input\\Names\invited_names.txt") as file:
    content = file.read()
    name_array = content.split("\n")

#Replace the [name] placeholder with the actual name.
for name in name_array:
    new_letter = letter_template.strip()
    new_letter = new_letter.replace("[name]", name)
    file_name = name.replace(" ", "")
    with open(f"Section24FilesDirectoriesAndPaths\MailMerge\Output\ReadyToSend\{file_name}.txt", "w") as file:
        file.write(new_letter)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp