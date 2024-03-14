from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
with open(r'c:\Users\Dell\Downloads\All AI tools List3.html', 'r', encoding='utf-8') as file:
    # Read the HTML content
    html_content = file.read()
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
span_elements = soup.find_all('i', class_='bi bi-heart float-end icons')
payment=soup.find_all('span',class_='badge float-end text-dark mr-2 pricing-badge')
description=soup.find_all('p',class_='my-1 mt-2 font-weight-lighter px-1')  
names=[]
links=[]
categories=[]
pay=[]
descriptions=[]
for i,j,k in zip(span_elements,payment,description):
    names.append(i['data-title'])
    links.append(i['data-website'])
    categories.append(i['data-tags'])
    pay.append(j.text.strip())
    descriptions.append(k.text.strip()[:-2])
names=np.array(names)
links=np.array(links)
categories=np.array(categories)
pay=np.array(pay)
descriptions=np.array(descriptions)
df=pd.DataFrame({'Tool Name':names,'Link':links,'Category':categories,'Description':descriptions,'payment':pay})
df.to_csv('sample3.csv',index=False)

    
