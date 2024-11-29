###
# Bubble sort
#
def bubble_sort(arr):
   n = len(arr)
   # Traverse through all array elements
   for i in range(n):
      # Last i elements are already in place
      for j in range(0, n-i-1):
         # Traverse the array from 0 to n-i-1
         # Swap if the element found is greater
         # than the next element
         if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions) 
print(sorted_bank_transactions)