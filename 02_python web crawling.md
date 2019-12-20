## Python web crawling

### 1. `requests` 모듈

- URL을 받아서 웹 페이지의 코드를 가져온다.

  ```python
  import requests # requests 모듈을 가져옴
  
  url = "http://finance.naver.com/marketindex/"
  # crawling할 웹 페이지의 주소를 url변수에 저장한다.
  
  req = requests.get(url).text
  # finance.naver.com/marketindex 페이지의 소스코드를 가져와 req에 저장한다.
  ```



## 2. `BeautifulSoup` 모듈

- `requests` 모듈로 받은 웹 페이지의 코드를 format(HTML, XML, JSON 등)에 맞게 파싱하고, 추출할 때 사용하는 모듈

- `excange.py` 예제 코드

  ```python
  import requests
  from bs4 import BeautifulSoup # bs4 모듈에서 Beautifulsoup 모듈을 가져옴
  
  url = "http://finance.naver.com/marketindex/"
  req = requests.get(url).text
  soup = BeautifulSoup(req, 'html.parser')
# html로 parsing해서 추출하기 좋은 형태로 바꾼다.
  
  exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
  # 추출한 데이터에서 HTML Tag 선택자를 이용하여 내가 원하는 정보를 하나만 가져온다.
  
  print(exchange.text)
  # exchange에 저장된 span태그의 속성인 text를 출력한다.
  ```
  



### 3. Python Web Crawling 예제

- `popularSearch.py` : 네이버 실시간검색어를 출력하는 예제

  ```python
  import requests
  from bs4 import BeautifulSoup
  url = "https://www.naver.com"
  
  req = requests.get(url).text
  soup = BeautifulSoup(req, 'html.parser')
  
  exchange = soup.select('.area_hotkeyword .ah_item > .ah_a > .ah_k')
  # 위의 exchange.py와 크게 다른 건 없지만, 이 부분이 다르다
  # soup 모듈의 select함수는 선택자에 의해 선택되는 모든 Element들을 exchange에 저장한다.
  
  for ps in exchange:
      print(ps.text)
  ```

