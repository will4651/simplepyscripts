#Script setup
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

#Scrape function assembles an array of srcs from images found in page and returns it
def scrape(url):
    req = Request(url, headers={'User-Agent' : "Browser"})
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    try:
        imgs = soup.find_all('img')
        srcs = []
        for count, item in enumerate (imgs, 0):
            srcs.append(str(item['src']))
            print(item['src'])
        return srcs
    except:
        return "There was an error with the URL. Check to make sure it's working and valid!"