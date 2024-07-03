import pandas as pd
import bs4 as BeautifulSoup
import requests
def text_mining(urls):
    data = []
    for url in urls:
        print(url)
        req = requests.get(url)
        c = req.content
        soup = BeautifulSoup(c, "html.parser")
        link = url
        title = soup.find('h1',class_="bbc-csfh25 e1p3vdyi0").text
        article_text = ''
        article = soup.find("div", {"class":"bbc-bg8vrv"}).findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        data.append({
            'Title':title,
            'Link':url,
            'Contents':article
            })
    df = pd.DataFrame(data).to_csv('news.csv',index=False)
    print(df)
    return article_text