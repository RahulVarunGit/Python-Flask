from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    #return("Hello World!")
    return render_template("index.html")

@app.route("/test")
def test():
    return("Hello World!")

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    #Check for empty script
    if not bool(city.strip()):
        city="New York"
    weather_data = get_current_weather(city)

    # City is not found by api
    if not weather_data['cod'] == 200:
        #return "city not found"
        return render_template("city-not-found.html")

    return render_template(
        "weather.html", title=weather_data["name"], 
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
   #app.run(host="0.0.0.0",port=8000)
   serve(app,host="0.0.0.0",port=8000)