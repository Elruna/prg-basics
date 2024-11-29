with open('countries.txt', 'r') as file:
   content = file.read()
   splited = content.splitlines()
   k=1
   for line in splited:
      print(k,end=line)
      k = k + 1