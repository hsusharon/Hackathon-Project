from flask import Flask, render_template, request, redirect, url_for
import urllib.request
from mainFunction import*
import re
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

twoDaysWeatherUrl = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-089?Authorization=CWB-7F744CE5-9B8A-4462-A344-727F6ECC932D&format=JSON"
todayWeatherUrl = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-7F744CE5-9B8A-4462-A344-727F6ECC932D&format=JSON"

twoDaysList=decodeUrl(twoDaysWeatherUrl,twoDaysWeatherSplitStr)
todayList=decodeUrl(todayWeatherUrl,todayWeatherSplitStr)



@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route('/country', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        for i in todayWeatherRemoveStr:
            for j in reversed(todayList):
                if(i==j):
                    todayList.remove(j)
        target = request.form['area']
        url = "https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.xml"

        req = urllib.request.Request(
            url,
            data=None,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
            }
        )
        res = urllib.request.urlopen(req)
        datab = res.read()
        data = datab.decode(encoding="utf-8",errors="ignore")
        list = data.split("<Name>")
        flag=0
        thep = []
        thea = []
        place = []
        area = []
        outward = []
        for x in list:
            index = x.split("</Name>")
            place.append(index[0])
            over = x.split("<Add>")
            for x in range(len(over)):
                if x==1:
                    getarea = over[x].split('</Add>')
                    str = getarea[0]
                    area.append(str[0:3])
        for i in range(len(area)):
            if area[i] == '臺北市' and target == "台北":
                outward.append(place[i+1])
                target2 = '臺北市'
            elif area[i] == '新北市' and target == "新北":
                outward.append(place[i+1])
                target2 = '新北市'
            elif area[i] == '新竹縣' and target == "新竹":
                outward.append(place[i+1])
                target2 = '新竹縣'
            elif area[i] == '桃園縣' and target == "桃園":
                outward.append(place[i+1])
                target2 = '桃園縣'
            elif area[i] == '苗栗縣' and target == "苗栗":
                outward.append(place[i+1])
                target2 = '苗栗縣'
            elif area[i] == '臺中市' and target == "台中":
                outward.append(place[i+1])
                target2 = '臺中市'
            elif area[i] == '彰化縣' and target == "彰化":
                outward.append(place[i+1])
                target2 = '彰化縣'
            elif area[i] == '雲林縣' and target == "雲林":
                outward.append(place[i+1])
                target2 = '雲林縣'
            elif area[i] == '南投縣' and target == "南投":
                outward.append(place[i+1])
                target2 = '南投縣'
            elif area[i] == '嘉義縣' and target == "嘉義":
                outward.append(place[i+1])
                target2 = '嘉義縣'
            elif area[i] == '臺南市' and target == "台南":
                outward.append(place[i+1])
                target2 = '臺南市'
            elif area[i] == '高雄市' and target == "高雄":
                outward.append(place[i+1])
                target2 = '高雄市'
            elif area[i] == '屏東縣' and target == "屏東":
                outward.append(place[i+1])
                target2 = '屏東縣'
            elif area[i] == '臺東縣' and target == "臺東":
                outward.append(place[i+1])
                target2 = '臺東縣'
            elif area[i] == '花蓮縣' and target == "花蓮":
                outward.append(place[i+1])
                target2 = '花蓮縣'
            elif area[i] == '澎湖縣' and target == "澎湖":
                outward.append(place[i+1])
                target2 = '澎湖縣'
        return render_template('/weather.html', target = target2, place = outward, todayList=todayList)
    else:
        return render_template('/country.html')

@app.route('/twoDaysWeather')
def twoDaysWeather():
    for i in twoDaysWeatherRemoveStr:
        for j in reversed(twoDaysList):
            if(i==j):
                twoDaysList.remove(j)
    return render_template("twoDaysWeather.html",twoDaysList=twoDaysList)
@app.route('/country')
def country():
    return render_template("country.html")
@app.route('/todayWeather')
def todayWeather():
    for i in todayWeatherRemoveStr:
        for j in reversed(todayList):
            if(i==j):
                todayList.remove(j)
    return render_template("todayWeather.html",todayList=todayList)

@app.route('/food', methods = ['POST', 'GET'])
def food():
    if request.method == 'POST':
        target = request.form['area']
        ind = []
        mus = []
        veg = []
        filename = 'india_export.json'
        with open(filename) as f:
            data = json.load(f)
            for i in data:
                name = i['餐廳名稱']
                ind.append(name)
                area = i['地區']
                ind.append(area)
        filename = 'taiwan.json'
        with open(filename) as f:
            data = json.load(f)
            for i in data:
                name = i['餐廳名稱']
                mus.append(name)
                area = i['地區']
                mus.append(area)
        filename = 'veg.json'
        with open(filename) as f:
            data = json.load(f)
            for i in data:
                name = i['客戶名稱']
                veg.append(name)
                area = i['地址']
                veg.append(area[0:3])
        return render_template('food.html', target = target, ind = ind, mus = mus, veg = veg)
    else:
        return render_template('foodCountry.html')
@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        target = request.form['area']
        title = []
        website=[]

        google_url = 'https://www.google.com.tw/search'

        word=target
        my_params = {'q': word}


        r = requests.get(google_url, params = my_params)



        if r.status_code == requests.codes.ok:

            soup = BeautifulSoup(r.text, 'html.parser')


            items = soup.select('div.g > h3.r > a[href^="/url"]')

            for i in range(10):
                title.append(items[i].text)
                website.append(items[i].get('href'))

        playplace=title[title.index(word+'10 大最佳旅遊景點- TripAdvisor')]
        playaddress=website[title.index(word+'10 大最佳旅遊景點- TripAdvisor')]
        return render_template("search.html", website = playaddress[7:])
    else:
        return render_template('country.html')   
if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/method', methods = ['GET', 'POST'])
# def method():
#     if(request.method == 'GET'):
#         return 'the method you use is ' + request.method
#     else:
#         return 'the method you use is  ' + request.method
# adj = 'dump ass'
# @app.route('/<username>')
# def profile(username):
#     return '<h2>hey there ' + username + ' ' + adj + '</h2>'
