import requests, json 
  
# Enter your API key here 
api_key = "b0ab939df7d8e8f185fe538d6a54bec5"  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def FindWeather(city_name):
  
    if(city_name == 'Banas Kantha'):
        city_name = 'Palanpur'
    if(city_name == 'Dangs'):
        city_name = 'Vyara'
    if(city_name == 'Kutch'):
        city_name = 'Bhuj'
    if(city_name == 'Narmada'):
        city_name = 'Bharuch'
    if(city_name == 'Dangs'):
        city_name = 'Vyara'
    if(city_name == 'Panchmahal'):
        city_name = 'Dahod'
    if(city_name == 'Sabarkantha'):
        city_name = 'Mahesana'
    if(city_name == 'Tapi'):
        city_name = 'Vyara'        
    
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 
  
    # json method of response object  
    # convert json format data into 
    # python format data 
    x = response.json() 
  
    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 
    if x["cod"] != "404": 
  
        coord = x["coord"]
        latitude = coord["lat"]
        longitude = coord["lon"]

        main = x["main"] 
        temperature = round(main["temp"] - 273,2)
        humidity = main["humidity"] 
        pressure = main["pressure"] 
  
        wind = x["wind"]
        wind_speed = round(wind["speed"] * 3.6,2)

        description = x["weather"] 
        weather_description = description[0]["description"] 

        lst = {'lat':latitude,'lon':longitude,'temp':temperature,'hum':humidity,'pres':pressure,'wspeed':wind_speed,'wdesc':weather_description}
        return lst
    
    else: 
        lst = {'lat':0,'lon':0,'temp':0,'hum':0,'pres':0,'wspeed':0,'wdesc':'City Not Found'}
        return lst 
