from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/opgg')
def opgg():
    userName = request.args.get('userName')
    url = f"http://www.op.gg/summoner/userName={userName}"
    req = requests.get(url).text
    data = BeautifulSoup(req, 'html.parser')

    rank_select = '#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank'
    rank = data.select_one(rank_select).text
    
    win_select = '#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins'
    win = data.select_one(win_select).text
    win = win[ :-1]

    
    # 등급과 승수를 자기 사이트에 출력하는 것
    
    return render_template('opgg.html', userName=userName, rank=rank, win=win)

if __name__ == ("__main__"):
    app.run(debug=True)