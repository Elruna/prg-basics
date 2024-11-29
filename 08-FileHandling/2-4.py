###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'
employees_file, "r"
# write selected employees to a file
with open(employees_file, "r") as file:
    content = file.read()
    lines = content.splitlines()
    with open(position_file, "w") as file:
      for line in lines:
         if job_title in line:
            file.write(f"{line}\n")