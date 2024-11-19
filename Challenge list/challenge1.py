# **Premier défi : Calculatrice de somme simple**

# Écris un programme Python qui :

# - Demande deux nombres à l'utilisateur.
# - Additionne ces deux nombres.
# - Affiche le résultat.

# Ce que tu apprends :

# - Les entrées et sorties (input/output) : Comprendre comment demander    une donnée à l'utilisateur (input) et afficher un résultat (print).
# - Les variables : Stocker et manipuler des valeurs.
# - Les types de données : Convertir des entrées en nombres (int ou float).

# C'est un exercice de base pour t'initier à la logique de programmation et à la syntaxe de Python. 


number_1 = input("Enter a number : ")
number_2 = input("Enter a second number : ")

number_1 = float(number_1)
number_2 = float (number_2)

print ("First number:", number_1)
print ("Second number:", number_2)

total = number_1 + number_2
print ("The sum is:", total)