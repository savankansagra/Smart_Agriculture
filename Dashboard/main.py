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
    return render_template('/home.html',pred = pred,data = data)

if __name__ == "__main__":
    app.run(debug=True)


print("this is from savan brach")

print("this is from savan_kansagrajhskdfj klsdkjfhashjfhjkshafdljlkjshaljk")
