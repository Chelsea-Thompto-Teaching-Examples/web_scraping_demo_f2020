# import required libraries
import requests
from bs4 import BeautifulSoup
import time

# download selected website
r = requests.get("https://www.sjsu.edu/")

# get the html code of the selected site
soup = BeautifulSoup(r.text, "html.parser")

# generate a list of elements on the site with the class "o-calender__date"
dates = soup.select(".o-calendar__date")

# create a task that runs for every item in dates
for d in dates:
	# for each item in the "dates" list, extract the text within the subclass "o-calender__day"
	day = d.select_one(".o-calendar__day").text
	# for each item in the "dates" list, extract the text within the subclass "o-calender__month"
	month = d.select_one(".o-calendar__month").text
	# print the text from "o-calender__month" and "o-calender__day" in the terminal window
	print(month, day)
	# pause the script for a half second to avoid overloading site
	time.sleep(0.5)