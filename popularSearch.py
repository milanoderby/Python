import requests
from bs4 import BeautifulSoup
url = "https://www.naver.com"

req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
exchange = soup.select('.area_hotkeyword .ah_item > .ah_a > .ah_k')
for ps in exchange:
    print(ps.text)
