from bs4 import BeautifulSoup
import requests
import csv
import os

#Location var
city = 'Berlin'
nation = 'Deutschland'

#Generate data for the first page
url = "https://housinganywhere.com/de/s/" + city + "--" + nation
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
   
#Initialize data of house listing by finding all listings in the webpage
listing = soup.findAll('a', attrs={'data-test-locator': 'Listing Card'})
price = []
warm = []
app_type = []
size = []
notation = []
date =[]
provider = []

for item in listing:
    price.append(item.contents[0].contents[1].contents[0].contents[0].contents[2].text[:5].rstrip(' €').rstrip('\xa0'))
    warm.append(item.contents[0].contents[1].contents[0].contents[0].contents[4].text)
    app_type.append(item.contents[0].contents[1].contents[1].contents[0].contents[0].text.rstrip(' •'))
    size.append(item.contents[0].contents[1].contents[1].contents[0].contents[1].text[:-3].rstrip(' '))
    if len(item.contents[0].contents[1].contents[1].contents[0]) > 3:
        notation.append(item.contents[0].contents[1].contents[1].contents[0].contents[2].text.rstrip(' •'))
        date.append(item.contents[0].contents[1].contents[1].contents[0].contents[3].text[3:].lstrip(' '))
    else:
        notation.append('')
        date.append(item.contents[0].contents[1].contents[1].contents[0].contents[2].text[3:].lstrip(' '))
    provider.append(item.contents[0].contents[1].contents[2].contents[0].contents[0].text)

#Find address of all listing
image = soup.findAll('img', attrs={'data-test-locator': 'ListingCardPhotoGallery/Photo'})
address = []

for item in image:
    address.append(item['title'].split(', ')[1])

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
    
    listing = soup.findAll('a', attrs={'data-test-locator': 'Listing Card'})

    for item in listing:
        price.append(item.contents[0].contents[1].contents[0].contents[0].contents[2].text[:5].rstrip(' €').rstrip('\xa0'))
        warm.append(item.contents[0].contents[1].contents[0].contents[0].contents[4].text)
        app_type.append(item.contents[0].contents[1].contents[1].contents[0].contents[0].text.rstrip(' •'))
        size.append(item.contents[0].contents[1].contents[1].contents[0].contents[1].text[:-3].rstrip(' '))
        if len(item.contents[0].contents[1].contents[1].contents[0]) > 3:
            notation.append(item.contents[0].contents[1].contents[1].contents[0].contents[2].text.rstrip(' •'))
            date.append(item.contents[0].contents[1].contents[1].contents[0].contents[3].text[3:].lstrip(' '))
        else:
            notation.append('')
            date.append(item.contents[0].contents[1].contents[1].contents[0].contents[2].text[3:].lstrip(' '))
        provider.append(item.contents[0].contents[1].contents[2].contents[0].contents[0].text)
    
    image = soup.findAll('img', attrs={'data-test-locator': 'ListingCardPhotoGallery/Photo'})

    for item in image:
        address.append(item['title'].split(', ')[1])
            
    links = soup.findAll('a', attrs={'data-test-locator': 'Listing Card'})
    hrefs = [item['href'] for item in links]
    for item in hrefs:
        x = item.split('/')
        ids.append(x[3].lstrip('ut'))

#Add all data to a table
columns = ['ID', 'Price', 'Housing Type', 'Size', 'Note', 'Provider Type', 'Address', 'Rent Price Info', 'Listing Date']
data = [ids, price, app_type, size, notation, provider, address, warm, date]
data = zip(*data)

#Save data to csv file
directory = f'data/{nation}/'
os.makedirs(directory, exist_ok=True)

with open(directory + city +'_housing_data.csv', 'w', newline='') as f:    
    # using csv.writer method from CSV package
    write = csv.writer(f)    
    write.writerow(columns)
    write.writerows(data)