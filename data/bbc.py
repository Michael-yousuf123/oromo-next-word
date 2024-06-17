import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
pages = set()
def getLinks(url):
    global pages
    html = urlopen('https://www.bbc.com/afaanoromoo.{}'.format(url))
    bs = BeautifulSoup(html, 'html.parser')

    for lin in bs.find_all('a', href=re.compile('^(/articles/)')):
        if 'href' in lin.attrs:
            if lin.attrs['href'] not in pages:
                newPage = lin.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
if __name__ == '__main__':
    getLinks("https://www.bbc.com/")
