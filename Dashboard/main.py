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
            'Season' : request.form["Crop"],
            'Crop' : request.form["Crop"],
            'avgTemp' : request.form["Crop"],
            'Cloud Cover' : request.form["Crop"],
            'maxTemp' : request.form["Crop"],
            'Precipitation' : request.form["Crop"],
            'vapPressure' : request.form["Crop"],
            'Rainfall' : request.form["Crop"],
            'Wet Day Freq' : request.form["Crop"],
            'minTemp' : request.form["Crop"]}
    pred = cyp.RFModel(data)
    return render_template('/home.html',pred = pred)

if __name__ == "__main__":
    app.run(debug=True)

