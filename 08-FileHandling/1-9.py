###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'
k = 0
with open("it_company.csv", "r") as file:
   file_content = file.read()
   file = file_content.splitlines()
   for line in file:
      if job_title in line:
         k += 1
print(k)