import lxml.html
from bs4 import BeautifulSoup
import requests
import re

year_list=list(range(2001,2018))
month_list=list(range(2,14))
for year in year_list:
    target_url = 'https://www.nhk.or.jp/bunken/yoron/political/2010.html'
    #Requestsを使って、webから取得
    r = requests.get(target_url)
    #要素を抽出
    soup = BeautifulSoup(r.content, 'lxml')



    # with open('https://www.nhk.or.jp/bunken/yoron/political/2010.html') as f :
    #     soup=BeautifulSoup(f,'html.parser')

    for div in soup.fing_all('tabel'):
        print(div.text)
# for td in soup in soup.parse('#main > div.section-plane > div > div.yoron-box-first > table > tbody > tr:nth-child(2)'):
    #     print(td)

        

    # html=tree.getroot()

    # for td in html in html.parse('#main > div.section-plane > div > div.yoron-box-first > table > tbody > tr:nth-child(2)'):
    #     print(td)


    # #main > div.section-plane > div > div.yoron-box-first > table > tbody > tr:nth-child(2) > td:nth-child(2)
    # #main > div.section-plane > div > div.yoron-box-first > table > tbody > tr:nth-child(2) > td:nth-child(13)