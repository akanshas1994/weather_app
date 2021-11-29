from flask import Flask,render_template,request
import requests

app=Flask(__name__)


@app.route("/")
def weather():
    
    
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city='city'
    weather_data=[]

    data=requests.get(url.format(city)).json()

    celcius=5/9*(data['main']['temp']-32)
    celcius=int(celcius)

    weather={
        'city':city,
        'temperature':celcius,
        'icon':data['weather'][0]['icon'],
        'description':data['weather'][0]['description']
    }
    weather_data.append(weather)

    print(data)
    return render_template('index.html',data=weather_data)

@app.route('/temp',methods=['POST'])
def temp():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city=request.form['city_name']
    weather_data=[]

    data=requests.get(url.format(city)).json()
    celcius=5/9*(data['main']['temp']-32)
    celcius=int(celcius)

    weather={
        'city':city,
        'temperature':celcius,
        'icon':data['weather'][0]['icon'],
        'description':data['weather'][0]['description']
    }
    weather_data.append(weather)

    print(data)
    return render_template('index.html',data=weather_data)
    



if(__name__)=="__main__":
 app.run(debug=True)