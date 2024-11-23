while True:
  try: 
    number = int(input("Please enter a number: "))

    if number < 0:
      print("Sorry, factorial does not exist for negative numbers")
    else :
      break
  except ValueError:
    print("Sorry, you did not enter a valid number")

factorial = 1

for i in range(1, number+1):
    factorial = factorial*i
    # We can also write 'factorial *= i' for more concise code

# Place the print statements outside the loop to avoid displaying intermediate results for each iteration.
print(f"{number}! is {factorial}")
print (f"Or we can also write that factorial of {number} is {factorial}")


# *= is an assignment operator : "x *= 3" = "x = x * 3"
# Example : 
# x = 5
# x *= 3
# print(x)
# 15
  