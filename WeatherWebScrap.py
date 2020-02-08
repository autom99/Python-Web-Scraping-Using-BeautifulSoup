import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast")
# print(week)

items = week.find_all(class_="tombstone-container")
# print(items)
# print(tonight.prettify())

period_names = [item.find(class_ ='period-name').get_text() for item in items]
short_description = [item.find(class_ ='short-desc').get_text() for item in items]
temperatures = [item.find(class_ ='temp').get_text() for item in items]

# print(period_names)
# print(short_description)
# print(temperatures)

weather_stuff = pd.DataFrame(
    {
        'Period': period_names,
        'Short Description': short_description,
        'Temperature': temperatures
    })
print(weather_stuff)
weather_stuff.to_csv('Weather.csv')
# weather_stuff.to_excel('Weather')


# Refer a URL: https://www.dataquest.io/blog/web-scraping-tutorial-python/
