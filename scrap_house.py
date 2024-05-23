from bs4 import BeautifulSoup
import requests
import csv

#Location var
city = 'Berlin'
nation = 'Deutschland'

#Generate data for the first page
url = "https://housinganywhere.com/de/s/" + city + "--" + nation
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#Initialize price list by finding all prices in the webpage
price = soup.findAll('div', attrs={'data-test-locator': 'ListingCardInfoPrice'})
price_list = []

for item in price:
    price_list.append(item.text[:5].rstrip(' €').rstrip('\xa0'))
    
#Initialize other data of house listing by finding all listings in the webpage
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

#Find ids of all listing     
links = soup.findAll('a', attrs={'data-test-locator': 'Listing Card'})
hrefs = [item['href'] for item in links]
ids = []

for item in hrefs:
    x = item.split('/')
    ids.append(x[3].lstrip('ut'))

#Find all the page to scrap through
buttons = soup.findAll('button')
p = []

for item in buttons:
    if len(item.text) <= 3 & len(item.text) != 0:
        p.append(item.text)
if p:
    lastPage = int(p.pop())
else:
    lastPage = 1
    
#Looping through all pages and add data to lists
for i in range(2, lastPage+1):
    url = ('https://housinganywhere.com/de/s/Berlin--Deutschland?page=' + str(i))
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    price = soup.findAll('div', attrs={'data-test-locator': 'ListingCardInfoPrice'})
    
    for item in price:
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

#Add all data to a table
columns = ['ID', 'Price', 'Housing Type', 'Size', 'Note']
data = [ids,price_list, app_type, size, notation]
data = zip(*data)

#Save data to csv file
with open('data/' + nation + '/' + city + '_housing_data.csv', 'w') as f:
    write = csv.writer(f)   
    write.writerow(columns)
    write.writerows(data)