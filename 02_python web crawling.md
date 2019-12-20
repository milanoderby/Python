## python web crawling

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

- `requests` 모듈로 받은 웹 페이지의 코드를 format(HTML, XML, JSON 등)에 맞게 파싱해온다.

  ```python
  import requests # requests 모듈을 가져옴
  
  url = "http://finance.naver.com/marketindex/"
  req = requests.get(url).text
  soup = BeautifulSoup(req, 'html.parser')
  ```

  
