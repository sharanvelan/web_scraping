from bs4 import BeautifulSoup
import json
import requests as req

url="https://www.wastedive.com/search/?q=epr"


data=[]

htmlfile=req.get(url).text
index=2
while True:


    doc=BeautifulSoup(htmlfile,"html.parser")

    list_of_article=doc.find('ul',class_="feed layout-stack-xxl").find_all('li',class_="row feed__item")


    for article in list_of_article:
        sub_data={}
        sub_data['title']=article.find('a').string.replace("\n","").replace(" ","")
        sub_data['url']="https://www.wastedive.com"+article.find('a')['href']
        sub_data['author']=article.find_all('span',class_="secondary-label")[0].string.replace("\n","").replace(" ","")
        sub_data['time']=article.find_all('span',class_="secondary-label")[1].string.replace("\n","").replace(" ","") if len(article.find_all('span',class_="secondary-label"))==2 else None

        if sub_data['time']==None:
            continue
    
        data.append(sub_data)
    
    response=req.get(f"https://www.wastedive.com/search/?page={index}&q=epr")
    
    if response.status_code!=200:
        break

    index+=1


# for one page 18  all 
  

with open('output.json','w') as file:
    file.write(json.dumps(data))
print(f"Total Article  -- {len(data)}")