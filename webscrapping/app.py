#webscrapping
import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com/questions")
result =response.text
soup = BeautifulSoup(result, "html.parser")
questions = soup.select(".s-post-summary")
for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".s-post-summary--stats-item-number").getText())