from flask import Flask, request, render_template, url_for, redirect
from Model_Package import CropYieldPrediction as cyp
from Model_Package import WeatherData as wd


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction" , methods = ["POST"])
def Crop_Prediction():
    if request.method == 'POST':
        data = {'City' : request.form["City"],
            'Year' : int(request.form["Year"]),
            'Season' : request.form["Season"],
            'Crop' : request.form["Crop"],
            'avgTemp' : int(request.form["avgTemp"]),
            'Cloud Cover' : int(request.form["Cloud Cover"]),
            'maxTemp' : int(request.form["maxTemp"]),
            'Precipitation' : int(request.form["Precipitation"]),
            'vapPressure' : int(request.form["vapPressure"]),
            'Rainfall' : int(request.form["Rainfall"]),
            'Wet Day Freq' : int(request.form["Wet Day Freq"]),
            'minTemp' : int(request.form["minTemp"])}
    pred = cyp.RFModel(data)
    return render_template('/prediction.html',pred = pred,data = data)

@app.route("/weather" , methods = ["POST"])
def Weather():
    if request.method == 'POST':
        Name = request.form["Name"]
        City = request.form["City"]
        Email = request.form["Email"]
        Area = float(request.form["Area"])
    lst = [Name,City,Email,Area]
    weatherdict = wd.FindWeather(City)
    return render_template('/home.html',lst = lst,dict= weatherdict)

@app.route("/p_redirect", methods = ["POST"])
def prediction_redirect():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)

