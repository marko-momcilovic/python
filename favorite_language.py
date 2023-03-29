favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
peoples = ['jen','marko','momca','phil']

for people in peoples:
    if people in favorite_languages.keys():
        print(f"Thanks ,{people.title()} for taking poll.")
    else:
        print(f"{people.title()} take the poll.")