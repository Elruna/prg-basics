categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
k=0
maxim = max(expenses)
for i in range(len(expenses)):
    if expenses[i] == maxim:
        k = i
print(categories[k])