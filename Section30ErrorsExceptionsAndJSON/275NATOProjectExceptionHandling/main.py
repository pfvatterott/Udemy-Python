import pandas
nato_data = pandas.read_csv("Section30ErrorsExceptionsAndJSON/275NATOProjectExceptionHandling/nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter:row.code for (index, row) in nato_data.iterrows()}

def print_nato_version():
    user_input = input("Enter a word: ").upper()
    try:
        code_list = [nato_dictionary[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        print_nato_version()
    else:
        print(code_list)

print_nato_version()