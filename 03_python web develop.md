## `Flask` 모듈

- ### Django`와 함께 자주 쓰이는 `python` 웹 개발 프레임워크

### 1. `flask` 를 활용한 웹 개발 기본 예제: `hello.py`

```python
from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
# 앞에 우리 홈페이지 주소가 생략되어있고, 그 뒤의 URI로 어떤 함수를 실행할 지 구분하여 실행한다.

def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    name="최용화"
    return render_template('hi.html', html_name = name)
# render_template은 현재 디렉토리가 아닌 하위의 templates 디렉토리에 html파일을 호출한다
# 호출 시, python 파일의 name 변수를 hi.html에 html_name이라는 변수로 넘겨준다.

@app.route('/greeting/<string:name>/')
# URI에 입력한 값을 string name으로 받아서 이를 function에서 이용한다.
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/fstring')
def fstring():
    fstring = "최용화"
    return f"제이름은 {fstring} 입니다."
# fstring 사용방법은 위와 같다.

@app.route('/cube/<int:num>')
# int 형으로 받는 것도 가능하다.
def cube(num):
    def_num = num**3
    return render_template('powerThree.html', origin_num=num, html_num=def_num)
# html에서 사용할 변수명은 내가 정해서 보내는 것이다.

@app.route('/dinner')
  def dinner():
      menu = ['삼각김밥', '컵라면', '스테이크', '마라탕', '훠궈']
      dinner = random.choice(menu)
      menu_img = {
          '삼각김밥': 'http://item.ssgcdn.com/96/16/97/item/1000024971696_i1_1200.jpg',
          '컵라면': 'http://image.auction.co.kr/itemimage/88/7a/1f/887a1f106.jpg',
          '스테이크': 'http://recipe1.ezmember.co.kr/cache/recipe/2017/07/09/6741acc7f6bf0f7d04245851fb365c311.jpg',
          '마라탕': 'https://m.6recipe.co.kr/web/product/big/201812/14d85a8d77aadf64de92851bbf94259a.jpg',
          '훠궈': 'http://d3b39vpyptsv01.cloudfront.net/0/0/1439790763299igBvjxI8NC.jpg',
      }
      return render_template('dinner.html', dinner=dinner, dinner_img=menu_img[dinner])
# 위의 함수처럼 img파일의 링크를 보내서 dinner.html에서 출력하는 것도 가능하다.    

if __name__=="__main__":
  	app.run(debug=True)
  # 이 코드가 있어서 python 이라는 명령어로 flask 코드를 실행할 수 있다.
  # ex) python hello.py
  # debug모드를 True로 해주는 이유는 debug모드를 실행시켜주지 않으면, 웹 서버가 실행되는동안 코드가 변경되도, 바로 반영이 되지 않아서 서버를 재기동해줘야 하기 때문이다.
  # 만약 이 코드가 없다면, 다음과 같이 실행해야 한다.
  # ex) env FLASK_APP=hello.py flask run
```



- `jinja` 문법: html코드 내에서 python문법을 사용하고 싶을 때 사용하는 문법

- `html` 코드 내에서 {% python code %} 이런 식으로 `python`코드를 감싸준다.

- `jinja` 문법 예제 `hello.py` 의 movies URL부분

  ```python
  @app.route('/movies')
    def movies():
        movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
        return render_template('movies.html', movies=movies)
      # 이 부분에서 movies라는 영화들을 list형태로 보내준다.
  ```

- `jinja` 문법 예제 `movies.html` 에서는 `movies`를 받아서 `jinja`문법을 이용하여 반복하여 출력한다.

  ```html
  <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    
    <body>
        <ul>
            {% for movie in movies %}
                {% if movie=='조커' %}
                    <li>{{movie}} || 이 영화 진짜 재밌어</li>
                {% elif movie=='겨울왕국2' %}
                    <li>{{movie}} || 올라프 커여워</li>
                {% else %}
                    <li>{{movie}}</li>
                {% endif %}
            {% endfor %}
        </ul>  
    </body>
    </html>
  ```

  

  ### 2. `Flask`의 `Get`방식을 이용한 웹 사이트 전환 예제 : `ping_pong.py`

- `ping_pong.py`

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return render_template('ping.html')
# [나의 서버 URL]/ping 으로 들어온 사용자에게 ping.html 을 보여준다.

@app.route('/pong')
def pong():
    data = request.args.get('keyword')
    # [나의 서버 URL]/ping 으로 들어온 사용자가 함께 가져온 keyword 변수를 받아서 data에 저장한다.
    return render_template('pong.html', data=data)
	# data 정보를 넘겨주고, pong.html을 완성한다.
    
@app.route('/naver')
def naver():
    return render_template('naver.html')

if __name__ == ("__main__"):
    app.run(debug=True)
```

- `ping.html` 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Here is Ping!!</h1>
    <form action="/pong">
        <input type="text" name="keyword">
        <input type="submit">
    </form>
    <!-- submit 버튼을 누르면 [기본 서버 URL]/pong 으로 이동하고, 이 때 text에 적힌 정보를 keyword라는 변수로 함께 전송한다.
        이 때, 전송되는 정보는 get방식이기 때문에 [기존 URL]/pong?keyword=[text에 입력한 정보] 이런 식으로 추가 정보를 전달한다. -->
</body>
</html>
```



