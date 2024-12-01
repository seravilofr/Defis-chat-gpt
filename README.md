Défis initiés par ChatGPT pour apprendre Python à partir du niveau débutant avec 1 ou 2 concepts à la fois.

Le prompt:  *"Sur cette page je vais te demander des défis pour apprendre python. Je suis débutant et je ne connais rien à Python donc chaque défi se concentrera sur un concept en partant de concepts simples et en allant de plus en plus compliqué. Donne moi mon premier défi et dis moi quel concept ça me permet d'apprendre"*


__________________________________

**Premier défi : Calculatrice de somme simple**

Écris un programme Python qui :

- Demande deux nombres à l'utilisateur.
- Additionne ces deux nombres.
- Affiche le résultat.

Ce que tu apprends :

- Les entrées et sorties (input/output) : Comprendre comment demander une donnée à l'utilisateur (input) et afficher un résultat (print).
- Les variables : Stocker et manipuler des valeurs.
- Les types de données : Convertir des entrées en nombres (int ou float).

C'est un exercice de base pour t'initier à la logique de programmation et à la syntaxe de Python. 



________________________

**Défi 2 : Convertisseur de températures**

Écris un programme Python qui :

- Demande à l'utilisateur une température en degrés Celsius.
- Convertit cette température en degrés Fahrenheit.
- Affiche le résultat.

La formule de conversion est : F=C×(9/5)+32

![](https://github.com/seravilofr/Defis-chat-gpt/blob/main/images/Celsius%20to%20Fahrenheit%20conversion.png?raw=true)

Ce que tu apprends avec ce défi :

- Opérations mathématiques : Comment utiliser des formules dans Python.
- Sortie formatée : Afficher un résultat avec du texte pour rendre la sortie plus lisible.
- S'assurer que tu maîtrises les bases : Manipulation des entrées, des variables et des types de données.

_______________________________

**Défi 3 : Vérification d’un nombre pair ou impair**

Écris un programme Python qui :

- Demande à l'utilisateur un nombre entier.
- Vérifie si ce nombre est pair ou impair.
- Affiche un message indiquant le résultat, comme :
  * "The number X is even."
  * "The number X is odd."

Ce que tu apprends avec ce défi :

- Structures conditionnelles : Utilisation de if et else pour prendre des décisions en fonction des données.
- Opérateurs mathématiques : Comprendre l'opérateur modulo (%) qui permet de savoir si un nombre est divisible par un autre.
- Types de données : Manipuler des nombres entiers avec int.

___________________________________________

**Défi 4 : Calculatrice de moyenne**

Écris un programme Python qui :

- Demande à l'utilisateur combien de notes il veut entrer.
- Permet à l'utilisateur d'entrer ces notes (une à une).
- Calcule la moyenne de ces notes et l'affiche.

Ce que tu apprends avec ce défi :

- Boucles : Utiliser une boucle pour demander plusieurs entrées de l'utilisateur.
- Listes : Stocker plusieurs valeurs dans une liste.
- Calculs avec des listes : Additionner les éléments d'une liste et calculer la moyenne.

_________________________________________________

**Défi 5 : Jeu de devinettes**

Crée un programme Python qui :

- Génère un nombre aléatoire entre 1 et 100 (inclus).
- Demande à l'utilisateur de deviner ce nombre.
- Informe l'utilisateur si sa réponse est trop haute, trop basse ou correcte.
- Continue jusqu'à ce que l'utilisateur trouve le bon nombre.
- Affiche le nombre de tentatives une fois que l'utilisateur a deviné correctement.

Ce que tu apprends avec ce défi :

- Modules Python : Utiliser le module random pour générer un nombre aléatoire.
- Boucles : Répéter une action jusqu'à ce qu'une condition soit remplie (while).
- Structures conditionnelles : Comparer les entrées utilisateur au nombre cible.

Exemple de fonctionnement attendu :

```
Guess the number (between 1 and 100): 50
Too high! Try again: 25
Too low! Try again: 30
Congratulations! You guessed the number in 3 attempts.
```

_____________________________________

**Défi 6 : Calcul de la factorielle d'un nombre**

Objectif : Écrire un programme qui calcule la factorielle d'un nombre donné par l'utilisateur. La factorielle d'un nombre entier positif n (notée n!) est le produit de tous les entiers de 1 à n. Par exemple :

```
5! = 5 * 4 * 3 * 2 * 1 = 120
``` 

Instructions :

- Demander à l'utilisateur de saisir un nombre entier positif.
- Calculer la factorielle de ce nombre en utilisant une boucle for.
- Afficher le résultat de la factorielle.

Concepts à utiliser :

- Les boucles for.
- La gestion des entrées utilisateur avec input().
- La conversion de la saisie de l'utilisateur en entier avec int().

_______________________________________________

**Défi 7 : Calculer la moyenne des nombres pairs dans une liste**

Écris un programme qui :

- Demande à l'utilisateur combien de nombres il veut ajouter dans une liste.
- Permet à l'utilisateur de saisir ces nombres un par un.
- Trouve tous les nombres pairs dans cette liste.
- Calcule et affiche la moyenne des nombres pairs (ou un message indiquant qu'il n'y a pas de nombres pairs).

Ce que tu apprendras :

- Gérer les listes en Python.
- Parcourir une liste avec une boucle.
- Utiliser des conditions pour filtrer des éléments (pairs).
- Gérer la division avec un cas spécial (éviter une erreur si aucun nombre pair n'est présent).

**Exemple attendu**

<ins>Entrée :</ins>

```
How many numbers do you want to add? 5
Enter number 1: 12
Enter number 2: 7
Enter number 3: 8
Enter number 4: 5
Enter number 5: 10
```

<ins>Sortie :</ins>

```
The even numbers are: [12, 8, 10]
The average of the even numbers is: 10.0
```

<ins>Entrée (aucun pair) :</ins>

```
How many numbers do you want to add? 3
Enter number 1: 1
Enter number 2: 3
Enter number 3: 5
```

<ins>Sortie :</ins>

```
There are no even numbers in the list.
```

_______________________________________

**Défi 8 : Compter les mots d'une phrase**

Écris un programme qui :

- Demande à l'utilisateur de saisir une phrase.
- Compte le nombre de mots dans cette phrase.
- Affiche le résultat.

Objectifs d'apprentissage :

- Manipulation des chaînes de caractères (str).
- Utilisation de la méthode .split() pour découper une chaîne en plusieurs parties.
- Utilisation des fonctions de base comme len() pour mesurer la longueur d'une liste.

**Exemple d'exécution :**

```
Enter a sentence: Python is fun to learn!
Your sentence contains 5 words.
```

