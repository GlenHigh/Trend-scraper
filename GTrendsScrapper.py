#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:37:56 2019

@author: glenhigh
"""

from selenium import webdriver 
from bs4 import BeautifulSoup
import pandas as pd
import os
os.chdir('/Users/glenhigh/Scrapping/GoogleTrends')



 #List to store name of the product
 #List to store price of the product
IS_SCRAPPED=False


if IS_SCRAPPED==False:
    driver = webdriver.Chrome(executable_path='/Users/glenhigh/Scrapping/GoogleTrends/chromedriver')
    #driver = webdriver.PhantomJS(executable_path='/Users/glenhigh/Scrapping/GoogleTrends/phantomjs') #Same without window opening
    print("Scrapping...")
    driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=FR&category=all")
    print("Scrapping ended")
    content = driver.page_source
    soup = BeautifulSoup(content)
    IS_SCRAPPED=True



i=1
titles=[]
for a in soup.findAll('div', attrs={'class':'details-top'}):
    titleParts=''
    for b in a.findAll('a'):
        titleParts=titleParts+str(b.contents[0][17:-15])+' '
    titles.append(titleParts)

print("Writing csv...")
df = pd.DataFrame({'Titles':titles}) 
df.to_csv('scrapped.csv', index=False, encoding='utf-8')
print("csv written")

print("Closing driver...")
driver.close
print("Driver closed")