try:
    file = open("Section30ErrorsExceptionsAndJSON/271CatchingExceptions/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError: #catches error
    print("there was an error")
    file = open("Section30ErrorsExceptionsAndJSON/271CatchingExceptions/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key does not exist. {error_message}")
else: #if no errors caught
    content = file.read()
    print(content)
finally: #happens no matter what
    file.close()
    print("File was closed")
    