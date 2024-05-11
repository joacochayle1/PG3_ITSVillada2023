from flask import Flask, render_template 
import requests 

app = Flask(__name__)

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dcdbf570b0b776f9cf13966415330f2f"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    city = 'London'
    weather_data = get_weather(city)
    return render_template('punto5.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)

