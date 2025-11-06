def icao(name):
    new_name = ''
    for char in name:
        new_name = new_name + char + " "
    return new_name
name = input("Write ur word: ")
print(f"Phonetic pronounce is {icao(name)}")