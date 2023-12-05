import requests
from bs4 import BeautifulSoup

URL = "https://rcdb.com/"


response = requests.get(URL)
steam_webpage = response.text
print(steam_webpage)

soup = BeautifulSoup(steam_webpage, "html.parser")
all_dates = soup.select("td time")
print(all_dates)
all_cities = soup.select("td")
cities_list = [city.get_text().split(')') for city in all_cities]
cities = cities_list[0]
print(cities)

dates = [date['datetime'].split('T')[0] for date in all_dates]
print(dates)

with open(file="rollercoaster_latest_additions.csv", mode="a", encoding="utf-8") as file:
    file.write("Date,Place\n")
    for i in range(len(dates)):
        file.write(f"{dates[i]},{cities[i]})\n")
