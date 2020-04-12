import random



#avgTemp	Cloud Cover	maxTemp	Precipitation	vapPressure	Rainfall	Wet Day Freq	minTemp
#print(fake.random_int(450,800))
def GetVariableData(city,season):
	if (city == 'Ahmedabad' or 'Gandhinagar' or 'Mahesana' or 'Panchmahal' or 'Dahod' or 'Kheda' or 'Sabarkantha'):
		if (season == 'Kharif'):
			avgTemp = round(random.uniform(27.5,30.5),2)
			CC = round(random.uniform(49,53),2)
			maxTemp = round(random.uniform(36.5,38),2)
			prec = round(random.uniform(410,580),2)
			vap = round(random.uniform(110,150),2)
			rain = round(random.uniform(480,650),2)
			wet = round(random.uniform(15,24),2)
			minTemp = round(random.uniform(21,25),2)
		if (season == 'Rabi'):
			avgTemp = round(random.uniform(23,25),2)
			CC = round(random.uniform(8.5,11.5),2)
			maxTemp = round(random.uniform(33.5,35),2)
			prec = round(random.uniform(10,15),2)
			vap = round(random.uniform(3,5),2)
			rain = round(random.uniform(1,19),2)
			wet = round(random.uniform(0,2),2)
			minTemp = round(random.uniform(13,16),2)
		if (season == 'Summer'):
			avgTemp = round(random.uniform(30,35),2)
			CC = round(random.uniform(18,24),2)
			maxTemp = round(random.uniform(40,45),2)
			prec = round(random.uniform(1,5),2)
			vap = round(random.uniform(1,5),2)
			rain = round(random.uniform(10,40),2)
			wet = round(random.uniform(0,1.5),2)
			minTemp = round(random.uniform(20,24),2)
		if (season == 'Whole Year'):
			avgTemp = round(random.uniform(24,28),2)
			CC = round(random.uniform(30,38),2)
			maxTemp = round(random.uniform(38,42),2)
			prec = round(random.uniform(180,210),2)
			vap = round(random.uniform(15,25),2)
			rain = round(random.uniform(190,250),2)
			wet = round(random.uniform(10,15),2)
			minTemp = round(random.uniform(13,16),2)
		
	elif (city == 'Kutch' or 'Banas Kantha' or 'Patan' or 'Surendranagar'):
		if (season == 'Kharif'):
			avgTemp = round(random.uniform(29.5,32.5),2)
			CC = round(random.uniform(47,51),2)
			maxTemp = round(random.uniform(38.5,40),2)
			prec = round(random.uniform(310,480),2)
			vap = round(random.uniform(95,130),2)
			rain = round(random.uniform(350,550),2)
			wet = round(random.uniform(9,20),2)
			minTemp = round(random.uniform(21,25),2)
		if (season == 'Rabi'):
			avgTemp = round(random.uniform(22,25),2)
			CC = round(random.uniform(8.5,11.5),2)
			maxTemp = round(random.uniform(34.5,36),2)
			prec = round(random.uniform(10,15),2)
			vap = round(random.uniform(3,5),2)
			rain = round(random.uniform(0,19),2)
			wet = round(random.uniform(0,2),2)
			minTemp = round(random.uniform(9,12),2)
		if (season == 'Summer'):
			avgTemp = round(random.uniform(35,38),2)
			CC = round(random.uniform(15,20),2)
			maxTemp = round(random.uniform(42,46),2)
			prec = round(random.uniform(1,5),2)
			vap = round(random.uniform(1,5),2)
			rain = round(random.uniform(10,20),2)
			wet = round(random.uniform(0,1.5),2)
			minTemp = round(random.uniform(12,24),2)
		if (season == 'Whole Year'):
			avgTemp = round(random.uniform(28,28),2)
			CC = round(random.uniform(30,38),2)
			maxTemp = round(random.uniform(42,46),2)
			prec = round(random.uniform(140,200),2)
			vap = round(random.uniform(15,25),2)
			rain = round(random.uniform(150,210),2)
			wet = round(random.uniform(10,12),2)
			minTemp = round(random.uniform(9,12),2)
		
	elif (city == 'Jamnagar' or 'Junagadh' or 'Porbandar' or 'Rajkot' or 'Amreli' or 'Bhavnagar'):
		if (season == 'Kharif'):
			avgTemp = round(random.uniform(26.5,32.5),2)
			CC = round(random.uniform(25,51),2)
			maxTemp = round(random.uniform(38.5,40),2)
			prec = round(random.uniform(500,1000),2)
			vap = round(random.uniform(50,100),2)
			rain = round(random.uniform(560,1100),2)
			wet = round(random.uniform(12,20),2)
			minTemp = round(random.uniform(21,25),2)
		if (season == 'Rabi'):
			avgTemp = round(random.uniform(22,25),2)
			CC = round(random.uniform(8.5,11.5),2)
			maxTemp = round(random.uniform(30.5,35),2)
			prec = round(random.uniform(10,15),2)
			vap = round(random.uniform(3,5),2)
			rain = round(random.uniform(0,19),2)
			wet = round(random.uniform(0,2),2)
			minTemp = round(random.uniform(12,15),2)
		if (season == 'Summer'):
			avgTemp = round(random.uniform(33,35),2)
			CC = round(random.uniform(15,20),2)
			maxTemp = round(random.uniform(40,44),2)
			prec = round(random.uniform(1,5),2)
			vap = round(random.uniform(10,15),2)
			rain = round(random.uniform(10,20),2)
			wet = round(random.uniform(0,1.5),2)
			minTemp = round(random.uniform(12,18),2)
		if (season == 'Whole Year'):
			avgTemp = round(random.uniform(27,30),2)
			CC = round(random.uniform(30,38),2)
			maxTemp = round(random.uniform(42,46),2)
			prec = round(random.uniform(200,500),2)
			vap = round(random.uniform(15,25),2)
			rain = round(random.uniform(250,600),2)
			wet = round(random.uniform(10,12),2)
			minTemp = round(random.uniform(12,18),2)

	elif (city == 'Anand' or 'Vadodara' or 'Bharuch' or 'Narmada'):
		if (season == 'Kharif'):
			avgTemp = round(random.uniform(26.5,32.5),2)
			CC = round(random.uniform(30,60),2)
			maxTemp = round(random.uniform(38.5,40),2)
			prec = round(random.uniform(800,1200),2)
			vap = round(random.uniform(50,110),2)
			rain = round(random.uniform(800,1200),2)
			wet = round(random.uniform(12,20),2)
			minTemp = round(random.uniform(21,25),2)
		if (season == 'Rabi'):
			avgTemp = round(random.uniform(22,25),2)
			CC = round(random.uniform(8.5,11.5),2)
			maxTemp = round(random.uniform(30.5,35),2)
			prec = round(random.uniform(10,15),2)
			vap = round(random.uniform(3,5),2)
			rain = round(random.uniform(0,19),2)
			wet = round(random.uniform(0,2),2)
			minTemp = round(random.uniform(12,15),2)
		if (season == 'Summer'):
			avgTemp = round(random.uniform(33,35),2)
			CC = round(random.uniform(15,20),2)
			maxTemp = round(random.uniform(40,44),2)
			prec = round(random.uniform(1,5),2)
			vap = round(random.uniform(10,15),2)
			rain = round(random.uniform(10,20),2)
			wet = round(random.uniform(0,1.5),2)
			minTemp = round(random.uniform(12,18),2)
		if (season == 'Whole Year'):
			avgTemp = round(random.uniform(27,30),2)
			CC = round(random.uniform(30,38),2)
			maxTemp = round(random.uniform(42,46),2)
			prec = round(random.uniform(300,600),2)
			vap = round(random.uniform(15,25),2)
			rain = round(random.uniform(300,600),2)
			wet = round(random.uniform(10,12),2)
			minTemp = round(random.uniform(12,18),2)

	elif (city == 'Surat' or 'Valsad' or 'Tapi' or 'Navsari' or 'Dangs'):
		if (season == 'Kharif'):
			avgTemp = round(random.uniform(24.5,28.5),2)
			CC = round(random.uniform(40,65),2)
			maxTemp = round(random.uniform(35.5,27),2)
			prec = round(random.uniform(850,1200),2)
			vap = round(random.uniform(25,60),2)
			rain = round(random.uniform(900,1400),2)
			wet = round(random.uniform(21,25),2)
			minTemp = round(random.uniform(21,25),2)
		if (season == 'Rabi'):
			avgTemp = round(random.uniform(22,25),2)
			CC = round(random.uniform(9,15),2)
			maxTemp = round(random.uniform(30.5,34),2)
			prec = round(random.uniform(10,15),2)
			vap = round(random.uniform(13,18),2)
			rain = round(random.uniform(10,20),2)
			wet = round(random.uniform(2,4),2)
			minTemp = round(random.uniform(12,15),2)
		if (season == 'Summer'):
			avgTemp = round(random.uniform(33,35),2)
			CC = round(random.uniform(15,20),2)
			maxTemp = round(random.uniform(38,40),2)
			prec = round(random.uniform(1,5),2)
			vap = round(random.uniform(10,15),2)
			rain = round(random.uniform(1,10),2)
			wet = round(random.uniform(0,1),2)
			minTemp = round(random.uniform(12,15),2)
		if (season == 'Whole Year'):
			avgTemp = round(random.uniform(25,28),2)
			CC = round(random.uniform(30,38),2)
			maxTemp = round(random.uniform(42,46),2)
			prec = round(random.uniform(600,950),2)
			vap = round(random.uniform(15,25),2)
			rain = round(random.uniform(600,950),2)
			wet = round(random.uniform(13,18),2)
			minTemp = round(random.uniform(12,18),2)

	VariableData = {
		'avgTemp':avgTemp,
		'Cloud Cover':CC,
		'maxTemp': maxTemp,
		'Precipitation':prec,
		'vapPressure':vap,
		'Rainfall':rain,
		'Wet Day Freq':wet,
		'minTemp':minTemp}
	return VariableData
