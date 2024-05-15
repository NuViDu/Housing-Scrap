from bs4 import BeautifulSoup
import requests
import csv


url = "https://housinganywhere.com/de/s/Berlin--Deutschland"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

price = soup.findAll('span', attrs={'data-test-locator': 'ListingCard.PriceLabel'})
price2 = soup.findAll('span', attrs={'data-test-locator': 'ListingCard.PriceLabel.DynamicMinPricing'})
price3 = soup.findAll('span', attrs={'data-test-locator': 'ListingCard.PriceLabel.PrecisePricing'})
price_list = []

for item in price:
    price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
for item in price2:
    price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
for item in price3:
    price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
    
listing = soup.findAll('div', attrs={'data-test-locator': 'ListingCardPropertyInfo'})
app_type = []
size = []
notation = []
date =[]

for item in listing:
    app_type.append(item.contents[0].text.rstrip(' •'))
    size.append(item.contents[1].text[:-3].rstrip(' '))
    notation.append(item.contents[2].text.rstrip(' •'))
    if len(item) > 3:
        date.append(item.contents[3].text[3:].lstrip(' '))
    else:
        date.append('')
        
links = soup.findAll('a', attrs={'data-test-locator': 'Listing Card'})
hrefs = [item['href'] for item in links]
ids = []

for item in hrefs:
    x = item.split('/')
    ids.append(x[3].lstrip('ut'))

buttons = soup.findAll('button')
p = []

for item in buttons:
    if len(item.text) <= 3 & len(item.text) != 0:
        p.append(item.text)
if p:
    lastPage = int(p.pop())
else:
    lastPage = 1
    
for i in range(2, lastPage+1):
    url = ('https://housinganywhere.com/de/s/Berlin--Deutschland?page=' + str(i))
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    price = soup.findAll('span', attrs={'data-test-locator': 'ListingCard.PriceLabel'})
    price2 = soup.findAll('span', attrs={'data-test-locator': 'ListingCard.PriceLabel.DynamicMinPricing'})
    price3 = soup.findAll('span', attrs={'data-test-locator': 'ListingCard.PriceLabel.PrecisePricing'})
    for item in price:
        price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
    for item in price2:
        price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
    for item in price3:
        price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
    
    listing = soup.findAll('div', attrs={'data-test-locator': 'ListingCardPropertyInfo'})
    for item in listing:
        app_type.append(item.contents[0].text.rstrip(' •'))
        size.append(item.contents[1].text[:-3].rstrip(' '))
        notation.append(item.contents[2].text.rstrip(' •'))
        if len(item) > 3:
            date.append(item.contents[3].text[3:].lstrip(' '))
        else:
            date.append('')
            
    links = soup.findAll('a', attrs={'data-test-locator': 'Listing Card'})
    hrefs = [item['href'] for item in links]
    for item in hrefs:
        x = item.split('/')
        ids.append(x[3].lstrip('ut'))

columns = ['ID', 'Price', 'Housing Type', 'Size', 'Note']
data = [ids,price_list, app_type, size, notation]
data = zip(*data)

with open('Berlin_housing_data.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write = csv.writer(f)
     
    write.writerow(columns)
    write.writerows(data)