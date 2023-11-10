import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
amount_of_letters = int(input("How many letters would you like in your password?\n"))
amount_of_symbols = int(input("How many symbols would you like?\n"))
amount_of_numbers = int(input("How many numbers would you like?\n"))

temp_password = ""
for number in range(0, amount_of_letters):
    randomInt = random.randint(0, len(letters) - 1)
    temp_password += letters[randomInt]

for number in range(0, amount_of_symbols):
    randomInt = random.randint(0, len(symbols) - 1)
    temp_password += symbols[randomInt]

for number in range(0, amount_of_numbers):
    randomInt = random.randint(0, len(numbers) - 1)
    temp_password += numbers[randomInt]
    

password_array = []
for letter in temp_password:
    password_array.append(letter)
random.shuffle(password_array)
password = "".join(password_array)
print(password)