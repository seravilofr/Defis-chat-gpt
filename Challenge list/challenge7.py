# Ask the user to input the number of values he want to add
while True:
  try:
    num_numbers = int(input("How many numbers do you want to add? "))
    break
  except ValueError:
    print("Please enter a correct value.")

# Ask the user the values
numbers_list = []
for i in range(num_numbers):
  while True:
    try:
      number = int(input(f"Please enter number {i+1}: "))
      numbers_list.append(number)
      break
    except ValueError:
      print("Please enter a whole number only.")

print(f"You entered the following numbers : {numbers_list}")

# Sort out the numbers that are even
even_list = []
for x in numbers_list:
  if x%2 == 0:
    even_list.append(x)
 # We can also write : even_list = [x for x in numbers_list if x % 2 == 0]

# Only print that if even_list exists (so if there is at least one even number)
if even_list:
  print(f"The even numbers are: {even_list}")
  

# Average calculation : 
# round = round a number to 2 decimals ; sum(even_list) = sum of the new list ; len(even_list) = Return the number of items in a list
if even_list:
  average = round(sum(even_list)/len(even_list), 2)
  print(f"The average of the even numbers is {average}.")
else:
  print("There are no even numbers in the list.")
