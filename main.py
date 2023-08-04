import requests
from bs4 import BeautifulSoup
import pandas

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movies_list = []

for movie_tag in movies:
    text = movie_tag.get_text()
    movies_list.append(text)

movies_list_data = pandas.DataFrame(movies_list)
movies_list_data = movies_list_data.iloc[::-1]  # This line of code was to make the csv file start from 1-100
movies_list_data.to_csv("movies_to_watch.csv", index=False)

# print(movies_list)


