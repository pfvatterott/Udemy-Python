import pandas
nato_data = pandas.read_csv("Section26ListComprehension\\244NatoAlphabetProject\\nato_phonetic_alphabet.csv")


# 1. Create a dictionary in this format:
nato_dictionary = {row.letter:row.code for (index, row) in nato_data.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
code_list = [nato_dictionary[letter] for letter in user_input]
print(code_list)
