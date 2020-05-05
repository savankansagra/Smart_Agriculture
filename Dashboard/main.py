from __future__ import print_function 
import sys
from flask import Flask, request, render_template, url_for, redirect, make_response, session
from Model_Package import CropYieldPrediction as cyp
from Model_Package import WeatherData as wd
from Model_Package import VariableAPI as varp
from Model_Package import Firebase as fb
from datetime import timedelta,datetime,date,time
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
uid = ''

app = Flask(__name__)
app.secret_key = 'kpkhant007'

@app.route("/")
def home():
    return render_template("index.html")


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

@app.route("/farm" , methods = ["POST"])
def Farm_Controller():
	if request.method == 'POST':
		Email = request.form["Email"]
		Password = request.form["Password"]
	auth = fb.getAuth(Email,Password)
	if(auth[0] == True):
		global uid
		uid = auth[1]
		session['username'] = Email
		data = fb.getData(auth[1])
		details = data['Details']
		soil_data = data['Soil_Parameter']
		motor = data['Controller']
		weatherdict = wd.FindWeather(details['City'])
		ontill = motor['OnTill']+timedelta(hours=5,minutes=30)
		laston = motor['LastOn']+timedelta(hours=5,minutes=30)
		current = datetime.now()
		return render_template("farmcontroller.html",uid = auth[1],data = data,name = details['Name'],city = details['City'], area = details['Land_Area'], email = details['Email'], mob = details['Mobile_No'],soilm = soil_data['Soil_Moisture'], temp = soil_data['Temprature'], hum = soil_data['Humidity'],status = motor['Status'], laston = laston, ontill = ontill,lat = weatherdict["lat"],lon = weatherdict["lon"])
	else:
		error = "Email or Password is incorrect"
		return render_template("farmlogin.html",error = error)

@app.route("/logout" , methods = ["POST"])
def Logout():
	if request.method == 'POST':
		session.clear()
		response =  render_template("farmlogin.html")
		response = make_response(response)
		response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
		return response

@app.route("/turnoff" , methods = ["POST"])
def Motor_off():
	if request.method == 'POST':
		global uid
		laston = ontill = datetime.now() - timedelta(hours=5,minutes=30)
		status = False
		data = {u'LastOn': laston,u'OnTill':ontill, u'Status':status}
		fb.updateData(uid,data)
		data = fb.getData(uid)
		details = data['Details']
		soil_data = data['Soil_Parameter']
		motor = data['Controller']
		weatherdict = wd.FindWeather(details['City'])
		ontill = motor['OnTill']+timedelta(hours=5,minutes=30)
		laston = motor['LastOn']+timedelta(hours=5,minutes=30)
		current = datetime.now()
		return render_template("farmcontroller.html",uid = uid,data = data,name = details['Name'],city = details['City'], area = details['Land_Area'], email = details['Email'], mob = details['Mobile_No'],soilm = soil_data['Soil_Moisture'], temp = soil_data['Temprature'], hum = soil_data['Humidity'],status = motor['Status'], laston = laston, ontill = ontill,lat = weatherdict["lat"],lon = weatherdict["lon"])

@app.route("/turnon" , methods = ["POST"])
def Motor_on():
	if request.method == 'POST':
		global uid
		hour = request.form["hour"]
		minute = request.form["minute"]
		laston = current = datetime.now() - timedelta(hours=5,minutes=30)
		ontill = current + timedelta(hours = int(hour), minutes = int(minute))
		status = True
		data = {u'LastOn': laston,u'OnTill':ontill, u'Status':status}
		fb.updateData(uid,data)
		data = fb.getData(uid)
		details = data['Details']
		soil_data = data['Soil_Parameter']
		motor = data['Controller']
		weatherdict = wd.FindWeather(details['City'])
		ontill = motor['OnTill']+timedelta(hours=5,minutes=30)
		laston = motor['LastOn']+timedelta(hours=5,minutes=30)
		current = datetime.now()
		return render_template("farmcontroller.html",uid = uid,data = data,name = details['Name'],city = details['City'], area = details['Land_Area'], email = details['Email'], mob = details['Mobile_No'],soilm = soil_data['Soil_Moisture'], temp = soil_data['Temprature'], hum = soil_data['Humidity'],status = motor['Status'], laston = laston, ontill = ontill,lat = weatherdict["lat"],lon = weatherdict["lon"])


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
        return render_template("farmlogin.html")
    elif request.form['redirect'] == 'Crop Prediction':
        return render_template("home.html")
    elif request.form['redirect'] == 'Back To Home':
        return render_template("index.html")
    elif request.form['redirect'] == 'GitHub Repository':
        return redirect(url_for("www.google.com"))


if __name__ == "__main__":
    app.run(debug=True)


