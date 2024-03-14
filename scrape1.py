import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
r = requests.get('https://aitools.fyi/', verify=False)
soup = BeautifulSoup(r.content, 'html.parser')
span_elements = soup.find_all('span', class_='space-x-1.5')
links1=soup.find_all('span',class_='hidden md:inline-block')
managements=soup.find_all('span',class_='inline-block font-[450] rounded text-sm mt-2 px-2 py-1 sm:px-2 sm:font-medium sm:py-1 break-words bg-transparent text-primary border-primary border shadow')
contents=[]
links2=[]
categories=[]
prices=[]
for i in span_elements:
    h2_elements = i.find_all('h2')
    links=i.find_all('a', href=True,attrs={"data-splitbee-event":"Premium Tool Click"})
    if h2_elements and links:
        content = h2_elements[0].text.strip()
        contents.append(content)
        links2.append(links[0]['href'])
    else:
        content = h2_elements[0].text.strip()
        contents.append(content)
for i in links1:
    link=i.find_all('a', href=True,attrs={"data-splitbee-event":"Tool Click"})
    links2.append(link[0]['href'])
j=0
for i in managements:
    if j%2==0:
        categories.append(i.text.strip())
    else:
        prices.append(i.text.strip())
    j+=1
contents=np.array(contents)
links2=np.array(links2)
categories=np.array(categories)
prices=np.array(prices)
df=pd.DataFrame({'Tool Name':contents,'Link':links2,'Category':categories,'Price':prices})
print(df)
df.to_csv('sample.csv',index=False)
    