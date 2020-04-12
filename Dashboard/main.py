from __future__ import print_function 
import sys
from flask import Flask, request, render_template, url_for, redirect, make_response
from Model_Package import CropYieldPrediction as cyp
from Model_Package import WeatherData as wd
from Model_Package import VariableAPI as varp
import pdfkit


ucity = ''
uarea = 0
uemail = ''
uname = ''
ulat = 0
ulon = 0
useason = ''
ucrop = ''
uyear = 0
upred = 0
utotal = 0


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/weather" , methods = ["POST"])
def Weather():
    if request.method == 'POST':
        Name = request.form["Name"]
        City = request.form["City"]
        Email = request.form["Email"]
        Area = float(request.form["Area"])
    lst = [Name,City,Email,Area]
    global ucity
    global uarea
    global uname
    global uemail
    global ulat
    global ulon
    ucity = City
    uarea = Area
    uemail = Email
    uname = Name
    weatherdict = wd.FindWeather(City)
    ulat = weatherdict["lat"]
    ulon = weatherdict["lon"]
    return render_template('/home.html',lst = lst,dict= weatherdict)


@app.route("/prediction" , methods = ["POST"])
def Crop_Prediction():
    if request.method == 'POST':
        Year = request.form["Year"]
        Season = request.form["Season"]
        if (Season == 'Kharif'):
            Crop = request.form["Kharif"]
        elif (Season == 'Rabi'):
            Crop = request.form["Rabi"]
        elif (Season == 'Summer'):
            Crop = request.form["Summer"]
        elif (Season == 'Whole Year'):
            Crop = request.form["Whole Year"]
        global ucity
        global uarea
        global uname
        global uemail
        global ulat
        global ulon
        global useason
        global ucrop
        global upred
        global utotal
        global uyear
        City = ucity
        var = varp.GetVariableData(City,Season)
        first = {'City':City,
        'Year': Year,
        'Season':Season,
        'Crop':Crop}
        data = {**first,**var}
    pred = cyp.RFModel(data)
    pred = round(((pred / 6.18) * 1000),3)
    total = round(pred * uarea,2)
    useason = Season
    ucrop = Crop
    upred = pred
    utotal = total
    uyear = Year
    return render_template('/prediction.html',pred = pred,total=total,ucity = ucity,uemail = uemail,uname = uname,uarea = uarea,ulat = ulat,ulon=ulon,season = Season,year = Year,crop = Crop)


@app.route("/redirect", methods = ["POST"])
def redirect1():
    if request.form['redirect'] == 'Predict Yield':
        return render_template("prediction.html")
    elif request.form['redirect'] == 'Download PDF':
    	global ucity
    	global uarea
    	global uname
    	global uemail
    	global ulat
    	global ulon
    	global useason
    	global ucrop
    	global upred
    	global utotal
    	global uyear
    	rendered = render_template('/pdf_template.html',upred = upred,utotal=utotal,ucity = ucity,uemail = uemail,uname = uname,uarea = uarea,ulat = ulat,ulon=ulon,useason = useason, uyear = uyear, ucrop = ucrop)
    	pdf = pdfkit.from_string(rendered,False)
    	response = make_response(pdf)
    	response.headers['Content-Type'] = 'application/pdf'
    	response.headers['Content-Disposition'] = 'inline, filename = report.pdf'
    	return response
    elif request.form['redirect'] == 'Farm Controller':
        return render_template("farmcontroller.html")
    elif request.form['redirect'] == 'Back To Home':
        return render_template("home.html")
    elif request.form['redirect'] == 'GitHub Repository':
        return redirect(url_for("www.google.com"))


if __name__ == "__main__":
    app.run(debug=True)


