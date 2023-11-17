with open('Section24FilesDirectoriesAndPaths\OpenReadWriteFiles\my_file.txt') as file:
    content = file.read()
    print(content)


with open('Section24FilesDirectoriesAndPaths\OpenReadWriteFiles\my_file.txt', mode="w") as file:
    file.write("New text")
    
    
    
with open('Section24FilesDirectoriesAndPaths\OpenReadWriteFiles\my_file.txt', mode="a") as file:
    file.write("\nAdded text")
    
    
with open("Section24FilesDirectoriesAndPaths\OpenReadWriteFiles\second_file.txt", mode="w") as file:
    file.write("New file text")