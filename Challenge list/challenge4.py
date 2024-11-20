try:
  grades_nb = int(input("How many grades to input? "))
  print(f"You will input {grades_nb} grades")

  grades_input = [] #crée liste "notes"

  for i in range(grades_nb):
      while True: #redemande en boucle une note qui ne serait pas bonne
        try:
          grade = float(input(f"Grade No.{i+1} : "))
          grades_input.append(grade)
          break  # quitte la boucle si la saisie est valide
        except ValueError:
          print("You did not input a correct grade")



  print(f"Here are the grades : {grades_input}") #mettre ce print hors de la boucle for pour que la liste s'affiche une seule fois

  somme = sum(grades_input)
  moyenne = round(somme/grades_nb, 2)
  print(f"Here is the average of the {grades_nb} grades: {moyenne}")


#Le bloc except fonctionne pour tout le code
except ValueError:
  print("You did not input a correct number of grades")