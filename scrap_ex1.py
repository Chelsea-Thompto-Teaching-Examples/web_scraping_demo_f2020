# import required libraries
import requests
from bs4 import BeautifulSoup

# download selected website
r = requests.get("https://www.sjsu.edu/")

# get the html code of the selected site
soup = BeautifulSoup(r.text, "html.parser")

# generate a list of elements on the site with the class "o-calender__date"
dates = soup.select(".o-calendar__date")

# create a task that runs for every item in dates
for d in dates:
	# print the text contained within the "o-calender__date" into the terminal window
	print(d.text)