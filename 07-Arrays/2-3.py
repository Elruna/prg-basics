# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
total = 0
for row in monthly_expenses:
    for item in row:
        total = total + item
total1 = 0
for row in monthly_expenses:
    for item in row:
        total1 = total1 + item
    break
total2 = 0
for row in range(3):
    total2 = total2 + monthly_expenses[1][row]
total3 = 0
for row in range(3):
    total3 = total3 + monthly_expenses[2][row]
total4 = 0
for row in range(3):
    total4 = total4 + monthly_expenses[3][row]
food = 0
for row in range(4):
    food = food + monthly_expenses[row][0]
trans = 0
for row in range(4):
    trans = trans + monthly_expenses[row][1]
uti = 0
for row in range(4):
    uti = uti + monthly_expenses[row][2]

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:',trans)
print('Utilities:',uti)
print('Week 1:',total1)
print('Week 2:',total2)
print('Week 3:',total3)
print('Week 4:',total4)
print('---------------')
print('TOTAL:',total)