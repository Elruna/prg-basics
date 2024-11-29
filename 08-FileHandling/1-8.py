###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

# calculates the total number of cars parked
total = 0
word_count = len(file_content.split())
total += word_count
print('Total cars parked:', total)