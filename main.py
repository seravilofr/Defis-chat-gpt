import random

solution = random.randint(1, 100)
# Uncomment the line below for debugging:
# print(solution)
attempts = 0

while True :
  try:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1 #Increment a counter
    
    #This block of code is: when the guess is correct it ends the loop
    if guess == solution:
      print(f"Congratulations, {solution} was the right answer !")
      print (f"You guessed it in {attempts} attempts")
      break
      
    elif guess > solution:
      print("The number is lower, please try again")
      print() # Add a blank line for better readability
    else:
      print("The number is higher, please try again")
      print() # Add a blank line for better readability
  except ValueError:
    print("You did not enter a valid number, try again")
  #If value is =/= solution, the loop goes back to the beginning (the input)


# We use an if/elif/else block instead of three separate if statements.  
# This stops Python from checking the other conditions as soon as one is true.  
# Example:  
# - If the guessed number is correct, Python skips the other conditions.  
# - This is faster and more logical because the three cases (equal, greater, smaller)  
#   are mutually exclusive (only one can be true at a time).  
  
            
  