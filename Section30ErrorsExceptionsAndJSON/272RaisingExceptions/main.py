# try:
#     file = open("Section30ErrorsExceptionsAndJSON/271CatchingExceptions/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError: #catches error
#     print("there was an error")
#     file = open("Section30ErrorsExceptionsAndJSON/271CatchingExceptions/a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key does not exist. {error_message}")
# else: #if no errors caught
#     content = file.read()
#     print(content)
# finally: #happens no matter what
#     raise KeyError("This is an error I made up")
    
    
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / (height * weight)
print(bmi)