try:
  name = int(input("Enter a whole number: "))
  print(f"You entered: {name}")

  if name%2 == 0:
    print ("Your number is even")
  else:
    print ("Your number is odd")

# En mettant except avant if la vérification de la condition est faite même s'il y a une erreur. Il faut donc mettre le except après la vérification comme ça
except ValueError:
  print ("You did not enter a valid number")