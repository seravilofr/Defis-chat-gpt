#On peut directement convertir l'input en float avec float(input()
celsius = float(input("Enter the temperature in Celsius : "))

#Du coup pas besoin de convertir celsius en float puisqu'on l'a déjà fait sur l'étape du dessus
fahrenheit = celsius*(9/5)+32

#Plutôt que print("Temperature in Fahrenheit:", fahrenheit,"°F") on utilise des f-strings qui permettent d'insérer directement des variables dans une chaîne :
print(f"Temperature in Celsius: {celsius}°C")
print(f"Temperature in Fahrenheit: {fahrenheit}°F")