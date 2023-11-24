from bs4 import BeautifulSoup


with open("Section45/373ParsingHTML/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
print(soup.prettify())
print(soup.title.string)
