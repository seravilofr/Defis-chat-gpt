# Défi 2 : Convertisseur de températures

# Écris un programme Python qui :

#     Demande à l'utilisateur une température en degrés Celsius.
#     Convertit cette température en degrés Fahrenheit.
#     Affiche le résultat.

# La formule de conversion est :
# F=C×(9/5)+32

# Ce que tu apprends avec ce défi :

#     Opérations mathématiques : Comment utiliser des formules dans Python.
#     Sortie formatée : Afficher un résultat avec du texte pour rendre la sortie plus lisible.
#     S'assurer que tu maîtrises les bases : Manipulation des entrées, des variables et des types de données.



#On peut directement convertir l'input en float avec float(input()
celsius = float(input("Enter the temperature in Celsius : "))

#Du coup pas besoin de convertir celsius en float puisqu'on l'a déjà fait sur l'étape du dessus
fahrenheit = celsius*(9/5)+32

#Plutôt que print("Temperature in Fahrenheit:", fahrenheit,"°F") on utilise des f-strings qui permettent d'insérer directement des variables dans une chaîne :
print(f"Temperature in Celsius: {celsius}°C")
print(f"Temperature in Fahrenheit: {fahrenheit}°F")