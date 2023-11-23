from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
    
yc_soup = BeautifulSoup(response.text, 'html.parser')

article_texts = []
article_links = []

article_tags = yc_soup.select(".title .titleline a")

for article in article_tags:
    if "from?" not in article.get("href"):
        article_link = article.get("href")
        article_text = article.getText()
        article_links.append(article_link)
        article_texts.append(article_text)


article_upvotes = [int(score.getText().split()[0]) for score in yc_soup.find_all(name="span", class_="score")]

highest_score = max(article_upvotes)
highest_score_index = article_upvotes.index(highest_score)

print(f"Title: {article_texts[highest_score_index]}\nLink: {article_links[highest_score_index]}\nScore: {highest_score}")