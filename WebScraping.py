from bs4 import BeautifulSoup
import requests #request establish an connection to the server and request library will make a GET request to a web server. which will downloand the html contents
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html") #select website
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

from bs4 import BeautifulSoup
import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p')[0].get_text()) #access elements individully and were using 0 to access the first element and use .get_text() to use method inside the p tag

print(soup.find_all('p', class_='outer-text')) #this will search through the doc and find all tags that has this class name


soup.find_all(id="first")#search by id will return a list and individual items in a list
#get_text() - we will get the infomation
#search by css selectors
    #soup.selct("css selectors")
