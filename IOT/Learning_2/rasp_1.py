# checking for Internet Connection
import urllib.request
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
import datetime
import Adafruit_DHT
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import time
import RPi.GPIO as GPIO


# initial setup of Pi
# GPIO.BCM means according to GPIO pins
GPIO.setmode(GPIO.BCM)
# motor_pump on GPIO 5 or pinlag=29
GPIO.setup(5, GPIO.OUT)


def check_wifi_is_connected():
    try:
        # request intenet to find the url and return its data
        print(urllib.request.urlopen('http://google.com'))
        return True
    except:
        return False


# check wifi is connected or not
# return :  True:- connected
#           False :- Not Connected
# check_wifi_is_connected()


# initialize cloud fire store
# Connect Pi to firebase using credentials
# which is json file :- credentials.json
# it return firestore client object
def connect_to_firebase():
    cred = credentials.Certificate("ServiceAccountKey.json")
    firebase_admin.initialize_app(cred)

    # initialize database connection
    db = firestore.client()
    # print(type(db))
    # <class 'google.cloud.firestore_v1.client.Client'>
    return db


#####
# Tocken for accesing the database

#####


# testing     done
def read_data(db, uid):
    user_ref = db.collection(uid)
    docs = user_ref.stream()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


# read_data(db)
#


# Synchronize the device condition with server at only one time
# On and off Motter according to Server Command.
# time interval to check motor is on or off = 5 minutes = 5 * 60 = 300 seconds.
# if time interval of motor in standard time interval then motor will on on
# else motor will be off
# if user forced to off motor then server last time will be off

def check_motor_state(db):
    motor_ref = db.collection(uid_token).document(u"Controller")
    motor_Data = motor_ref.get()
    if motor_Data.exists:
        print("motor data : {}".format(motor_Data.to_dict()))

    # motor last means current statues
    motor_last_statues = motor_Data.to_dict().get(u"Status")
    print(motor_last_statues)

    # motor last On time
    motor_lastOn_time = motor_Data.to_dict().get(u"LastOn")
    # convert google datetime object into python datetime object
    motor_lastOn_time_datetime = datetime.datetime.combine(date=motor_lastOn_time.date(
    ), time=motor_lastOn_time.time(), tzinfo=motor_lastOn_time.tzinfo)

    # motor till on time
    motor_Ontill_time = motor_Data.to_dict().get(u"OnTill")
    # convert google datetime object into python datetime object
    motor_Ontill_time_datetime = datetime.datetime.combine(date=motor_Ontill_time.date(
    ), time=motor_Ontill_time.time(), tzinfo=motor_Ontill_time.tzinfo)

    # getting current time from firebase Server
    current_datetime = datetime.datetime.utcnow()
    current_datetime = current_datetime.replace(tzinfo=datetime.timezone.utc)
    # print(current_datetime.tzinfo)
    # print(motor_lastOn_time_datetime.tzinfo)
    # print(motor_Ontill_time_datetime.tzinfo)
    # print(motor_lastOn_time_datetime)
    # print(current_datetime)
    # print(motor_Ontill_time_datetime)

    # if current_datetime in interval of Onmotor then
    # Onmotor pin on raspberry pi
    # update status on firebase
    if current_datetime < motor_Ontill_time_datetime and current_datetime > motor_lastOn_time_datetime:
        # motor pin on = 32
        GPIO.output(5, GPIO.HIGH)

        # update status on firebase
        motor_ref.update(
            {u'Status': True}
        )
    else:
        # motor pin off = 32
        GPIO.output(5, GPIO.LOW)
        motor_ref.update(
            {u'Status': False}
        )


# read sensor data and send to Server
def read_and_send_sernsordata(db, uid):
    # tempreture reading function
    # args:
    #   sensor :- we use DHT11 so sensor = 11
    #   pin :- we connecected DHT11 to GPIO 4
    # return:
    #   tempreture,humidity
    def read_tempreture(sensor=11, pin=4):
        humidity, tempreture = Adafruit_DHT.read_retry(sensor, pin)
        print("Temp :{0:0.1f} C         Humidity{1:0.1f} %".format(
            tempreture, humidity))
        return tempreture, humidity

    # soil moisture reading using Adafruit_MCP3008
    # args:
    #       pin_number = MCP Output channel number = default 0
    # return:
    #       soil moisture in range 200 to 1100
    #       dry > 600   around 1000 in air
    #       wet < 600   around 200 in full water
    def read_soil_moisture(pin_number=0):
        # software SPI configuration
        # bydefault for MCP3008
        CLK = 18
        MISO = 23
        MOSI = 24
        CS = 25
        mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

        # read value
        val = mcp.read_adc(pin_number)
        return val

    # Dictoanry for all 3 values
    # {Humidity: 35, Soil_Mositure:210, Tempreture:35.1}
    temprature_, humidity_ = read_tempreture(sensor=11, pin=4)
    soil_moisture_ = read_soil_moisture(pin_number=0)

    soil_data_dict = {
        u"Humidity": humidity_,
        u"Soil_Mositure": soil_moisture_,
        u"Tempreture": temprature_
    }

    # create refrence to Soil_Parameter and
    # update data on firebase
    Soil_Parameter_ref = db.collection(uid).document(u"Soil_Parameter")
    Soil_Parameter_ref.update(soil_data_dict)


#
#####################
# Main Function that call abouve all function and perform operation
if __name__ == "__main__":
    while True:
        check_wifi_is_connected()
        db = connect_to_firebase()
        uid_token = u'VA85MuoofzZiR1LKm7CT30GngWs2'
        read_data(db, uid_token)
        # GPIO PINS FOR
        # tempreture sensor ( DHT11 ) = GPIO-4
        # Soil_Mositure Sensor        = MCP channel 0
        #                               CLK = 18
        #                               MISO = 23
        #                               MOSI = 24
        #                               CS = 25
        check_motor_state(db)
        read_and_send_sernsordata(db, uid_token)
        # sleep for 5 minutes
        time.sleep(5*60)
