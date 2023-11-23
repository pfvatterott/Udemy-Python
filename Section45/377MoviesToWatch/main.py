import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


movie_response = requests.get(URL)
movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

movie_title_elems = movie_soup.find_all(name="h3", class_="title")
movie_title_elems.reverse()
movie_titles = ""
for title in movie_title_elems:
    title_text = title.getText()
    movie_titles += f"{title_text}\n"
    
    
    
print(movie_titles)

with open("Section45/377MoviesToWatch/movies.txt", "w") as file:
    file.write(movie_titles)