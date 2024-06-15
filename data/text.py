from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

namelist = bs.find_all('class', {'class':'green'})

for name in namelist:
    print(name.get_text())