from bs4 import BeautifulSoup
import requests
from datetime import datetime
from datetime import timedelta
import json

start_date = "2017-2-01"
end = datetime.today()
start = datetime.strptime(start_date, "%Y-%m-%d")
fishArr = []

while start < end:
    date = start.strftime("%Y-%m-%d")
    url = 'https://www.apvigo.es/es/lalonjahoy/ventas/dia=' + date
    response = requests.get(url,timeout=10)
    soup = BeautifulSoup(response.content,"html.parser")
    fixedsoup = soup.find('tbody')

    for fishData in fixedsoup.find_all('tr'):
        fishObject = {
          "date":date,
          "name":fishData.findAll('td')[0].text,
          "maxPrice":fishData.findAll('td',attrs={"class":"cantidad"})[0].text,
          "minPrice":fishData.findAll('td',attrs={"class":"cantidad"})[1].text,
          "quantity":fishData.findAll('td',attrs={"class":"cantidad"})[2].text
        }
        fishArr.append(fishObject)
        print(fishObject)
    start = start + timedelta(days=1)

with open('fishVigo.json','w') as outfile:
    json.dump(fishArr,outfile)
