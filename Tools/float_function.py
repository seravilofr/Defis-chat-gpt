# Function to "block" the user if they input something other than a float

def prompt_float(string msg): float
  while true:
      try:
          return float(input(msg))
      except:
          print("Error in value")