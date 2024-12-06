price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
k=0
k1=0
for items, count in price_list.items():
   k = k + count
   print(f"The count of {items} is {count}")
print(k)
for items, count in price_list.items():
   count = count*0.9
   k1 = k1 + count
   print(f"The count of {items} is {count}")
print(k1)
   
