# I have a webinar from the good folks at Antisyphon/BHIS coming up the tomorrow. 
# Was wondering how many fully free courses they have in a year so I could attend them all, since I don't have a job so far.
# I'm feeling adventurous, might try this using powershell next.
from bs4 import BeautifulSoup
import requests
soup =  BeautifulSoup(requests.get('https://www.antisyphontraining.com/training-calendar/list/?tribe_eventcategory%5B0%5D=125').text, 'html.parser') #125 is possibly for "Pay what you can" events
#xpath magic (find divs containing the events)
events = soup.find_all('div', class_='tribe-events-calendar-list__event-wrapper')
for event in events:
    #more xpath magic (filter spans in each event that contain the price, the free events have no such elements, so we compare with None)
    if(event.find("span", class_="tribe-events-c-small-cta__price")==None):
        #even more xpath magic (print the name of the event)
        print(event.find("a", class_='tribe-events-calendar-list__event-title-link tribe-common-anchor-thin').text.strip())