from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "ef9a3d31837bf5a5ea1f5085a43aab92"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if request.method == "POST":
        city = request.form["city"]
        response = requests.get(
            f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "City not found!"}

    return render_template("index.html", weather_data=weather_data, current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
