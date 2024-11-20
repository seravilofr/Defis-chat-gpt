try:
  nb_notes = int(input("Combien de notes à saisir? "))
  print(f"Vous allez saisir {nb_notes} notes")

  notes_saisies = [] #crée liste "notes"

  for i in range(nb_notes):
      while True: #redemande en boucle une note qui ne serait pas bonne
        try:
          note = float(input(f"Note n°{i+1} : "))
          notes_saisies.append(note)
          break  # quitte la boucle si la saisie est valide
        except ValueError:
          print("Vous n'avez pas saisi une note valide")



  print(f"Voici les notes saisies : {notes_saisies}") #mettre ce print hors de la boucle for pour que la liste s'affiche une seule fois

  somme = sum(notes_saisies)
  moyenne = round(somme/nb_notes, 2)
  print(f"Voici la moyenne des {nb_notes} notes: {moyenne}")


#Le bloc except fonctionne pour tout le code
except ValueError:
  print("Vous n'avez pas saisi un nombre valide")