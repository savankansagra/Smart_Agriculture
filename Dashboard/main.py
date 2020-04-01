from flask import Flask, request, render_template, url_for, redirect
from Model_Package import CropYieldPrediction as cyp

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/" , methods = ["POST"])
def Crop_Prediction():
    if request.method == 'POST':
        data = {'City' : request.form["City"],
            'Year' : request.form["Year"],
            'Season' : request.form["Season"],
            'Crop' : request.form["Crop"],
            'avgTemp' : request.form["avgTemp"],
            'Cloud Cover' : request.form["cloudcover"],
            'maxTemp' : request.form["maxTemp"],
            'Precipitation' : request.form["precipitation"],
            'vapPressure' : request.form["vapPressure"],
            'Rainfall' : request.form["Rainfall"],
            'Wet Day Freq' : request.form["Wet Day Freq"],
            'minTemp' : request.form["minTemp"]}
    pred = cyp.RFModel(data)
    return render_template('/home.html',pred = pred)

if __name__ == "__main__":
    app.run(debug=True)
