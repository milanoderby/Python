from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

@app.route('/')
# 앞에 우리 홈페이지 주소가 생략되어있고, 그 뒤의 URI로 어떤 함수를 실행할 지 구분하여 실행한다.

def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
#

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

@app.route('/movies')
def movies():
    movies = ['조커', '겨울왕국2', '터미네이터', '어벤져스']
    return render_template('movies.html', movies=movies)

if __name__=="__main__":
	app.run(debug=True)
# 이 코드가 있어서 python 이라는 명령어로 flask 코드를 실행할 수 있다.
# ex) python hello.py
# 만약 이 코드가 없다면, 다음과 같이 실행해야 한다.
# ex) env FLASK_APP=hello.py flask run