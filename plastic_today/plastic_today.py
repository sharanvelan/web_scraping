from bs4 import BeautifulSoup
import json
import requests

url="https://www.plasticstoday.com/search/node/epr"

data=[]

html_file=requests.get(url).text

doc=BeautifulSoup(html_file,"html.parser")

    # print(doc.find('article',class_="article-teaser__search article-teaser article-teaser__icon__article"))
articles=doc.find_all('article',class_="article-teaser__search article-teaser article-teaser__icon__article")

for article in articles:
    sub_data={}

    sub_data['title']=article.find('div',class_="title").a.string
    sub_data['url']="https://www.plasticstoday.com"+article.find('div',class_="title").a['href']
    sub_data['meta']=article.find('div',class_='summary-wrapper').string
    sub_data['img_url']=article.find('img')['data-src']
    sub_data['date']=article.find('span',class_='date').string

    print(sub_data)

    data.append(sub_data)
      

    
print(len(data))

with open('output.json','w') as file:
    file.write(json.dumps(data))
