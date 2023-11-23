from bs4 import BeautifulSoup


with open("Section45/374SelectingElementsWithSoup/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
    
    
heading = soup.find_all(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")

headings = soup.select(".heading")
print(headings)