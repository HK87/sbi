# SBI証券で取り扱っている米国株のTickerと説明文を取得する

import requests
from bs4 import BeautifulSoup

target_url = 'https://search.sbisec.co.jp/v2/popwin/info/stock/pop6040_usequity_list.html'
r = requests.get(target_url)
r.encoding = 'shift_jis'

soup = BeautifulSoup(r.text, 'lxml')


for tr in soup.find_all('tr'):
    ticker_row = tr.find('th', class_='vaM alC')
    if ticker_row is None:
        continue
    for td in tr.findAll('td'):
        if td.find('br') is None and not td.attrs:
            print(f"{ticker_row.text},{td.text}")
        
