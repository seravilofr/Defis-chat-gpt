import string # Useful to import the string.punctuation constant that has all the punctuation signs


# Ask the user to input a sentence
sentence_input = str(input("Please enter a sentence: "))
print(f"Original sentence: {sentence_input}")

# Remove punctuation from the sentence
sentence_input_clean = sentence_input.translate(str.maketrans('', '', string.punctuation))
print (f"Cleaned sentence: {sentence_input_clean}")

# Create a list of each word after cleaning
word_list = sentence_input_clean.split()
print (f"Word list: {word_list}")

# Calculate length of list = number of workds
number_words = len(word_list)
print(f"Your sentence contains {number_words} words.")