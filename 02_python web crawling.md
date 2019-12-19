## python web crawling

### 1. `requests` 모듈

- url을 받아서 웹 페이지의 코드를 가져온다.

  ```python
  import requests
  
  url = "http://finance.naver.com/marketindex/"
  req = requests.get(url).text
  ```



## 2. `BeautifulSoup` 모듈

- `requests` 모듈로 받은 웹 페이지의 코드를 format(HTML, XML, JSON 등)에 맞게 파싱해온다.

  ```python
  import requests
  
  url = "http://finance.naver.com/marketindex/"
  req = requests.get(url).text
  soup = BeautifulSoup(req, 'html.parser')
  ```

  

## 3. `Flask` 모듈

