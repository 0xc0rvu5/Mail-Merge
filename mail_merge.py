#initialize global variable
PLACEHOLDER = "[name]"


#obtain invite list
with open("./Input/Names/invite_list.txt") as names_file:
    names = names_file.readlines()


#obtain template, fix readability, replace PLACEHOLDER with names then proceed to write files.
with open("./Input/Letters/letter_template.txt") as f:
    content = f.read()
    for name in names:
        stripped_name = name.strip()
        official_letter = content.replace(PLACEHOLDER, stripped_name)
        print(official_letter)
        with open(f"./Output/Send/letter_for_{stripped_name}.txt", mode="w") as completed:
            completed.write(official_letter)
