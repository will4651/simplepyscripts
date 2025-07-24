#Script setup
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://neumont.smartcatalogiq.com/en/2022-2023/catalog/academic-calendar/'
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")

#Scrape function assembles a string with necessary elements and returns it
def scrape():
    div = soup.find('div', {'class': {'combinedChild'}})
    tables = div.find_all('table')
    text = ''

    for i1, item in enumerate(tables, 0):
        text += f'{tables[i1].caption.string}\n'
        tr = tables[i1].tbody.find_all('tr')

        for i2, item in enumerate(tr, 0):
            td = tr[i2].find_all('td')
            text += f'{td[0].string}: {td[1].string}\n'
        text += '\n'
    return text