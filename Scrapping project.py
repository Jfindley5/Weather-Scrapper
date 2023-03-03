from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

#use find all method to get all the list elements
seven_day = soup.find(id="seven-day-forecast-list")
forecast_items = seven_day.find_all(class_="tombstone-container")

#scrap the first day info
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

img = tonight.find("img")
desc = img['title']

#instead of doing that for the rest of the days in the week, well use the css selector method to get the list items quickly in a list
#this for loop - t will trverse through the list made by css selector
# and each tile it will call a t.get_text() which we'll get enterign inside all the othe rlist variable.
# so we don't have to write much code and itll be clean and clear
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#now we're converting it into pandas data frame with these list. DF is in the form of a dictionary.
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})

#create the csv file, we call the csv method
weather.to_csv('weather.csv')

